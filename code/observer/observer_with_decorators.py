
def observable(cls):

    cls._observers = []
    cls._metrics = dict()

    def register_observer(self, observer):
        self._observers.append(observer)

    def unregister_observer(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._metrics)

    cls.register_observer = register_observer
    cls.unregister_observer = unregister_observer
    cls.notify = notify

    return cls


class Observable():

    _observers = []
    _metrics = dict()

    def register_observer(self, observer):
        self._observers.append(observer)

    def unregister_observer(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._metrics)


class WeatherData(Observable):
    _metrics = {"temperature": 0}

    def set_temperature(self, new_temp):
        self._metrics["temperature"] = new_temp
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
