import kivy

from kivy.properties import StringProperty, NumericProperty
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
import requests
from modules.weather_kv import WeatherData


kivy.require('1.5.0')


class DeviceLayout(GridLayout):
    """The main layout."""

    city = StringProperty()
    current_temp = StringProperty()
    min_temp = StringProperty()
    max_temp = StringProperty()
    icon_id = StringProperty()

    def _request_weather_data(self):
        """TODO: Docstring for request_weather.
        :returns: TODO

        """
        requested_location = 'Dachau'
        api_key = ''

        try:
            with open('resources/api.txt') as f:
                api_key = f.readline()
        except FileNotFoundError:
            print('The api key is not found')

        print(api_key)
        api_url = 'http://api.openweathermap.org/data/2.5/weather'
        payload = {'q': requested_location, 'APPID': api_key, 'units': 'metric'}
        r = requests.get(api_url, params=payload)
        print(r.url)
        print(r.json())

        weather = WeatherData(r.json())
        print(weather.city)
        self.city = weather.city
        self.current_temp = weather.temp
        self.min_temp = weather.min_temp
        self.max_temp = weather.max_temp
        self.icon_id = weather.icon

    def load(self):
        self._request_weather_data()


class InfoDeviceApp(App):
    """The main Kivy App"""

    def build(self):
        """Build the main App.
        :returns: DeviceLayout

        """
        parent = DeviceLayout()
        parent.load()

        return parent


def main():
    InfoDeviceApp().run()
