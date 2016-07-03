"""
    Copyright (C) 2016  Richard Schwalk

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from PyQt5.QtCore import QObject, QTimer, pyqtSignal, pyqtProperty, pyqtSlot, \
    QUrl, QJsonDocument, qDebug, QAbstractListModel, Qt, QDateTime, QVariant
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from enum import Enum, unique

from PyQt5.QtQml import QQmlListProperty


class WeatherController(QObject):
    """
    Class to request the weather data and control the view
    """

    # noinspection PyUnresolvedReferences
    def __init__(self, parent=None):
        super(WeatherController, self).__init__(parent)

        self._dataReceived = False
        self._forecastDataReceived = False

        self._weather_data = CurrentWeatherData()
        self._weather_forecast_data = []
        self._data_model = ForecastDataModel()

        self._network_manager = QNetworkAccessManager(self)
        self._timer = QTimer(self)

        self._timer.timeout.connect(self.update_weather)

        self._current_weather = None
        self._forecast_weather = None
        self._api_key = ''

        try:
            with open('resources/api.txt') as f:
                self._api_key = f.readline()
        except FileNotFoundError:
            print('The api key is not found')

    weather_changed = pyqtSignal()

    @pyqtProperty('QString', notify=weather_changed)
    def location(self):
        return self._weather_data.location_name

    @pyqtProperty('QString', notify=weather_changed)
    def description(self):
        return self._weather_data.description

    @pyqtProperty('QString', notify=weather_changed)
    def icon(self):
        return self._weather_data.icon

    @pyqtProperty('QString', notify=weather_changed)
    def temp(self):
        return str(self._weather_data.temperature)

    model_changed = pyqtSignal()

    @pyqtProperty(QQmlListProperty, notify=model_changed)
    def data_model(self):
        return QQmlListProperty(ForecastDataModel,
                                self,
                                self._weather_forecast_data)

    @pyqtSlot()
    def view_is_ready(self):
        """
        Request the weather data and start the timer when the view is ready,
        called from the view onCompleted.

        :rtype: none
        """
        self._request_weather_data()
        self._timer.start(3600000)

    @pyqtSlot()
    def stop_timer(self):
        pass

    def weather_data_received(self):
        json_str = self._current_weather.readAll()
        json_doc = QJsonDocument.fromJson(json_str)
        self._read_current_weather_data(json_doc.object())

    def forecast_data_received(self):
        json_str = self._forecast_weather.readAll()
        json_doc = QJsonDocument.fromJson(json_str)
        self._read_forecast_data(json_doc.object())

    def update_weather(self):
        pass

    def _read_current_weather_data(self, json_object):
        # location
        """
        Read the current weather data from the json object.

        :param json_object: The Json Object
        :return nothing
        """
        if 'name' not in json_object:
            self._weather_data.location_name = 'No data available!'
        else:
            name = json_object['name'].toString()
            qDebug(name)
            if name == '':
                message = json_object['message'].toString()
                self._weather_data.location_name = message
            else:
                self._weather_data.location_name = name

                # temperature
                tDo = json_object['main'].toObject()['temp'].toDouble()
                temp = int(round(tDo))
                self._weather_data.temperature = temp

                # description
                json_weather = json_object['weather'].toArray()[0].toObject()
                desc = json_weather['description'].toString()
                self._weather_data.description = desc

                # icon
                icon = json_weather['icon'].toString()
                icon_path = '../resources/weather_img/{0}.png'.format(icon)
                self._weather_data.icon = icon_path

            self.weather_changed.emit()

    def _read_forecast_data(self, json_object):
        json_list = json_object['list'].toArray()
        self._weather_forecast_data.clear()
        for obj in json_list:
            json_list_object = obj.toObject()
            forecast_data = WeatherForecastData()

            # time
            time = json_list_object['dt'].toInt()
            forecast_data.time = time

            weather_array = json_list_object['weather'].toArray()
            weather_object = weather_array[0].toObject()

            # description
            desc = weather_object['description'].toString()
            forecast_data.description = desc

            # icon
            icon = weather_object['icon'].toString()
            icon_path = '../resources/weather_img/{0}.png'.format(icon)
            forecast_data.icon = icon_path

            # temperature max / min
            temp_object = json_list_object['temp'].toObject()
            temp_min_double = temp_object['min'].toDouble()
            temp_max_double = temp_object['max'].toDouble()
            temp_min = int(round(temp_min_double))
            forecast_data.temp_min = temp_min
            temp_max = int(round(temp_max_double))
            forecast_data.temp_max = temp_max

            self._weather_forecast_data.append(forecast_data)

        self._data_model.set_all_data(self._weather_forecast_data)
        self.model_changed.emit()

    def _request_weather_data(self):
        """
        Request the weather over Http request at openweathermap.org, you need
        an API key according to use the services.
        If the call is finished will call according function over Qt's
        signaling System.

        :return: nothing

        """

        # request current weather
        api_call = QUrl(
            'http://api.openweathermap.org/data/2.5/weather?q'
            '=Dachau,de&units=metric&APPID={0}'.format(self._api_key))
        request_current_weather = QNetworkRequest(api_call)
        self._current_weather = self._network_manager.get(
            request_current_weather)
        self._current_weather.finished.connect(self.weather_data_received)

        # forecast data
        api_call_forecast = QUrl(
            'http://api.openweathermap.org/data/2.5/forecast/daily?q=Dachau,'
            'de&cnt=4&units=metric&APPID={0}'.format(self._api_key))
        request_forecast = QNetworkRequest(api_call_forecast)
        self._forecast_weather = self._network_manager.get(request_forecast)
        self._forecast_weather.finished.connect(self.forecast_data_received)


@unique
class RoleNames(Enum):
    TempRole = Qt.UserRole
    DescriptionRole = Qt.UserRole + 1
    TimeRole = Qt.UserRole + 2
    IconRole = Qt.UserRole + 3


class ForecastDataModel(QAbstractListModel):
    """Docstring for ForecastDataModel. """

    def __init__(self, parent=None):
        super(ForecastDataModel, self).__init__(parent)
        self._role_names = {
            RoleNames.TempRole: 'temp',
            RoleNames.DescriptionRole: 'description',
            RoleNames.TimeRole: 'time',
            RoleNames.IconRole: 'icon',
        }
        self._data = []

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self._data)

    def data(self, QModelIndex, role=None):
        row = QModelIndex.row()

        if row < 0 or row >= len(self._data):
            return QVariant()

        if role == RoleNames.IconRole:
            return self._data[row].icon
        elif role == RoleNames.TempRole:
            return ForecastDataModel.format_temp(self._data[row])
        elif role == RoleNames.DescriptionRole:
            return self._data[row].description
        elif role == RoleNames.TimeRole:
            return ForecastDataModel.format_time(self._data[row])

        return QVariant()

    def set_all_data(self, data):
        self.beginResetModel()
        self._data.clear()
        self._data = data
        self.endResetModel()

    @staticmethod
    def format_temp(weather):
        return '{0} °C / {1} °C'.format(weather.temp_max, weather.temp_min)

    @staticmethod
    def format_time(weather):
        dt = QDateTime.fromTime_t(weather.time)
        return dt.toString('dddd')

    def roleNames(self):
        return self._role_names


class BaseWeatherData:
    def __init__(self):
        self._description = ''
        self._icon = ''

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value


class CurrentWeatherData(BaseWeatherData):
    def __init__(self):
        super(CurrentWeatherData, self).__init__()
        self._temperature = 0
        self._location = ''

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value

    @property
    def location_name(self):
        return self._location

    @location_name.setter
    def location_name(self, value):
        self._location = value


class WeatherForecastData(BaseWeatherData):
    """Docstring for WeatherForecastData. """

    def __init__(self):
        """TODO: to be defined1. """
        super(WeatherForecastData, self).__init__()
        self._temp_min = 0
        self._temp_max = 0
        self._time = 0

    @property
    def temp_min(self):
        return self._temp_min

    @temp_min.setter
    def temp_min(self, value):
        self._temp_min = value

    @property
    def temp_max(self):
        return self._temp_max

    @temp_max.setter
    def temp_max(self, value):
        self._temp_max = value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value
