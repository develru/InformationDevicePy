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
    QUrl, QJsonDocument
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest


class WeatherController(QObject):
    """
    Class to request the weather data and control the view
    """

    # noinspection PyUnresolvedReferences
    def __init__(self, parent=None):
        super(WeatherController, self).__init__(parent)

        self._network_manager = QNetworkAccessManager(self)
        self._timer = QTimer(self)

        self._timer.timeout.connect(self.update_weather)

        self._current_weather = None
        self._api_key = ''

        try:
            with open('resources/api.txt') as f:
                self._api_key = f.readline()
        except FileNotFoundError:
            print('The api key is not found')

    weather_changed = pyqtSignal()

    @pyqtProperty('QString', notify=weather_changed)
    def location(self):
        pass

    @pyqtProperty('QString', notify=weather_changed)
    def description(self):
        pass

    @pyqtProperty('QString', notify=weather_changed)
    def icon(self):
        pass

    @pyqtProperty('QString', notify=weather_changed)
    def temp(self):
        pass

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
        self._read_data(json_doc.object())

    def forecast_data_received(self):
        pass

    def update_weather(self):
        pass

    def _read_data(self, json_object):
        name = json_object['name'].toString()
        print(type(name), name, '\n')

    def _read_forecast_data(self, json_object):
        pass

    def _request_weather_data(self):
        api_call = QUrl('http://api.openweathermap.org/data/2.5/weather?q' \
                        '=Dachau,de&units=metric&APPID={0}'.format(
                        self._api_key))
        request_current_weather = QNetworkRequest(api_call)
        self._current_weather = self._network_manager.get(
            request_current_weather)
        self._current_weather.finished.connect(self.weather_data_received)