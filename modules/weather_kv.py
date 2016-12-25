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

    @property
    def city(self):
        return self._city
