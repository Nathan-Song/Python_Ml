class WeatherData():

    def __init__(self):
        self._observers = []
        self._temperature = None

    def register_observer(self, observer):
        self._observers.append(observer)

    def unregister_observer(self, observer):
        self._observers.remove(observer)

    def notify(self):

        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, new_temp):
        self._temperature = new_temp
        self.notify()


class TemperatureDisplay():
    def update(self, temperature):
        print(f"Temperature changed to: {temperature} °C")


temperature_watcher = TemperatureDisplay()

weather = WeatherData()
weather.register_observer(temperature_watcher)

weather.set_temperature(10)
weather.set_temperature(20)
weather.set_temperature(10)
