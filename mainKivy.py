import kivy

kivy.require('1.5.0')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
import requests
from modules.weather_kv import WeatherData


class DeviceLayout(GridLayout):
    """The main layout."""

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
