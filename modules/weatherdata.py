
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
from enum import Enum, unique
from PyQt5.QtCore import Qt, QAbstractListModel, QObject, QVariant, QDateTime


@unique
class RoleNames(Enum):
    TempRole = Qt.UserRole
    DescriptionRole = Qt.UserRole + 1
    TimeRole = Qt.UserRole + 2
    IconRole = Qt.UserRole + 3


class ForecastDataModel(QAbstractListModel, QObject):
    """Docstring for ForecastDataModel. """

    def __init__(self, parent=None):
        super(ForecastDataModel, self).__init__(parent)
        self._role_names = {
            RoleNames.TempRole.value: b'temp',
            RoleNames.DescriptionRole.value: b'description',
            RoleNames.TimeRole.value: b'time',
            RoleNames.IconRole.value: b'icon',
        }
        self._data = []

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self._data)

    def data(self, QModelIndex, role=None):
        row = QModelIndex.row()

        if row < 0 or row >= len(self._data):
            return QVariant()

        if role == RoleNames.IconRole.value:
            return self._data[row].icon
        elif role == RoleNames.TempRole.value:
            return ForecastDataModel.format_temp(self._data[row])
        elif role == RoleNames.DescriptionRole.value:
            return self._data[row].description
        elif role == RoleNames.TimeRole.value:
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
