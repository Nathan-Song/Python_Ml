
# Python Schulung: Aggregation und Komposition

## Einführung

In der objektorientierten Programmierung (OOP) sind Aggregation und Komposition zwei Formen der Assoziation, die beschreiben, wie Klassen und Objekte miteinander verbunden sind. Diese Konzepte sind entscheidend, um komplexe Softwarearchitekturen zu entwerfen.

## Unterschiede zwischen Aggregation und Komposition

### Aggregation

- **Definition**: Aggregation ist eine Beziehung, bei der das Ganze (Container) und die Teile (Inhalte) eine has-a-Beziehung haben, aber unabhängig voneinander existieren können.
- **Lebensdauer**: Die Teile können unabhängig vom Ganzen existieren.

```python
class Engine:
    def start(self):
        print("Engine starting")

class Car:
    def __init__(self, engine):
        self.engine = engine

engine = Engine()
car = Car(engine)
```

### Komposition

- **Definition**: Komposition ist eine strengere Form der Aggregation, bei der die Teile nicht ohne das Ganze existieren können.
- **Lebensdauer**: Wenn das Ganze zerstört wird, werden auch die Teile zerstört.

```python
class Wheel:
    def __init__(self):
        print("Wheel created")

class Car:
    def __init__(self):
        self.wheels = [Wheel() for _ in range(4)]

    def __del__(self):
        print("Car destroyed along with its wheels")
```

## Anwendung in Python

### Beispielprojekt: Fahrzeugverwaltungssystem

- **Aggregation**: Ein Auto hat einen Motor. Der Motor kann unabhängig vom Auto existieren.
- **Komposition**: Ein Auto besteht aus Rädern. Die Räder existieren nicht unabhängig vom Auto.

### Codebeispiel

```python
class Engine:
    def __init__(self, model):
        self.model = model

    def start(self):
        print(f"Engine {self.model} starting")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Aggregation
        self.wheels = [Wheel() for _ in range(4)]  # Komposition

    def start(self):
        print("Car starting")
        self.engine.start()

engine = Engine("V8")
car = Car(engine)
car.start()
```

## Fazit

Das Verständnis von Aggregation und Komposition ermöglicht es Python-Entwicklern, effizientere und strukturiertere Anwendungen zu entwerfen. Diese Konzepte sind essentiell für die Erstellung von wartbaren und erweiterbaren Codebasen in der OOP.
