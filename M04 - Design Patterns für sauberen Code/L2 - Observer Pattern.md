
# Python Schulung

## Observer Pattern – Implementierung und Anwendung des Beobachtermusters

Das Observer Pattern, oder Beobachtermuster, ist ein Entwurfsmuster, das ein Eins-zu-viele-Verhältnis zwischen Objekten definiert. Wenn sich der Zustand eines Objekts ändert, werden alle abhängigen Objekte benachrichtigt und automatisch aktualisiert. Dieses Muster ist besonders nützlich in Event-Driven-Programmen oder wenn eine Änderung in einem Objekt andere Objekte informieren und aktualisieren muss.

## Kernkonzepte

### Subjekt (Observable)

Das Subjekt oder Observable ist das Objekt, dessen Zustand sich ändert. Es verwaltet eine Liste von Beobachtern und benachrichtigt diese, wenn eine Änderung stattfindet.

```python
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)
```

### Beobachter (Observer)

Ein Beobachter registriert sich beim Subjekt und wird benachrichtigt, wenn sich der Zustand des Subjekts ändert. Dies erfolgt durch eine `update`-Methode, die der Beobachter implementieren muss.

```python
class Observer:
    def update(self, subject):
        pass

class ConcreteObserver(Observer):
    def update(self, subject):
        print(f"Observer received update: {subject._state}")
```

### Anwendung

Das Beobachtermuster wird oft verwendet, wenn ein Objekt verschiedene Teile einer Anwendung informieren muss, ohne von ihnen abhängig zu sein.

### Beispiel: Temperaturüberwachungssystem

In diesem Beispiel haben wir ein Temperaturüberwachungssystem, bei dem mehrere Displays (Beobachter) über die aktuelle Temperatur (Subjekt) informiert werden.

```python
class TemperatureSensor(Subject):
    def __init__(self):
        super().__init__()
        self._state = 0

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.notify()

class TemperatureDisplay(Observer):
    def update(self, subject):
        print(f"Temperature updated to: {subject.state}°C")

# Nutzung
sensor = TemperatureSensor()
display1 = TemperatureDisplay()
display2 = TemperatureDisplay()

sensor.attach(display1)
sensor.attach(display2)

sensor.state = 25  # Displays erhalten die Benachrichtigung und zeigen "25°C"
sensor.state = 30  # Displays zeigen nun "30°C"
```

## Praktische Anwendung

Das Beobachtermuster wird in vielen realen Anwendungen verwendet, z.B. in grafischen Benutzeroberflächen (GUIs), Event-Management-Systemen und in der Implementierung von Model-View-Controller (MVC)-Architekturen. Es hilft dabei, lose gekoppelte Systeme zu erstellen, in denen sich die Komponenten unabhängig voneinander entwickeln und ändern können.

## Fazit

Das Observer Pattern ist ein essenzielles Muster, das in vielen Python-Anwendungen nützlich ist. Durch das Verständnis und die Anwendung dieses Musters können Entwickler flexiblere und modularere Software entwerfen.
