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


class WeatherData(object):
    """Class to hold the current weather data"""

    def __init__(self, json_object=None):
        if json_object is None:
            print('Invalid use of Weather Data, initialize with JSON data.')
        else:
            self._city = json_object['name']
            self._temp = '{0:.0f}'.format(round(json_object['main']['temp'], 0))
            self._min_temp = '{0:.0f}'.format(round(json_object['main']['temp_min'], 0))
            self._max_temp = '{0:.0f}'.format(round(json_object['main']['temp_max'], 0))
            main_weather = json_object['weather'][0]
            self._icon = main_weather['icon']
            self._description = main_weather['main'] + ' (' + main_weather['description'] + ')'

    @property
    def city(self):
        return self._city

    @property
    def temp(self):
        return self._temp

    @property
    def min_temp(self):
        return self._min_temp

    @property
    def max_temp(self):
        return self._max_temp

    @property
    def icon(self):
        return self._icon

    @property
    def description(self):
        return self._description
