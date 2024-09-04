
# Python Code Examples from Presentation - Day 2

## Modul 4: Design Patterns für sauberen Code

### Lab 4.1: Factory Pattern – Erzeugungsmuster für flexible und wiederverwendbare Objekte

#### Code 1: Einfaches Factory Pattern

```python
class Hund:
    def make_sound(self):
        return "Wuff"

class Katze:
    def make_sound(self):
        return "Miau"

class TierFactory:
    @staticmethod
    def get_tier(tier_typ):
        if tier_typ == "Hund":
            return Hund()
        elif tier_typ == "Katze":
            return Katze()
        else:
            return None

# Beispielhafte Nutzung:
tier = TierFactory.get_tier("Hund")
print(tier.make_sound())
```

### Lab 4.2: Observer Pattern – Implementierung und Anwendung des Beobachtermusters

#### Code 2: Einfaches Observer Pattern

```python
class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        pass

class ConcreteObserver(Observer):
    def update(self, message):
        print(f"Received message: {message}")

# Beispielhafte Nutzung:
subject = Subject()
observer = ConcreteObserver()
subject.add_observer(observer)
subject.notify_observers("Hallo Welt")
```

### Lab 4.3: Singleton Pattern – Sicherstellen dass eine Klasse nur ein einziges Objekt erstellt

#### Code 3: Singleton Pattern

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

# Beispielhafte Nutzung:
singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # Ausgabe: True
```

## Modul 5: Metaklassen und Deskriptorklassen

### Lab 5.1: Metaklassen – Die dynamische Erstellung und Anpassung von Klassen

#### Code 4: Einfaches Beispiel für eine Metaklasse

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.greet = lambda self: f"Hallo, {self.__class__.__name__}!"
        return x

class Person(metaclass=Meta):
    pass

# Beispielhafte Nutzung:
person = Person()
print(person.greet())  # Ausgabe: Hallo, Person!
```

### Lab 5.2: Deskriptorklassen – Kontrollierter Zugriff auf Attribute und deren Einsatzmöglichkeiten

#### Code 5: Deskriptor für schreibgeschützte Attribute

```python
class ReadOnlyDescriptor:
    def __init__(self, initial_value=None):
        self._value = initial_value

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        raise AttributeError("This attribute is read-only")

class MyClass:
    readonly = ReadOnlyDescriptor("Initial Value")

# Beispielhafte Nutzung:
obj = MyClass()
print(obj.readonly)  # Ausgabe: Initial Value
obj.readonly = "New Value"  # Löst AttributeError aus
```

### Lab 5.3: Klassenabstraktion und -hierarchien

#### Code 6: Abstrakte Klassenhierarchie

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Wuff"

class Cat(Animal):
    def sound(self):
        return "Miau"

# Beispielhafte Nutzung:
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.sound())
```

## Modul 6: Typsicherheit und Projektorganisation

### Lab 6.1: Typsicherheit in Python

#### Code 7: Verwendung von Type Hints

```python
def multiply(a: int, b: int) -> int:
    return a * b

# Beispielhafte Nutzung:
result = multiply(2, 3)
print(result)  # Ausgabe: 6
```

### Lab 6.2: Vom Code zur Distribution: Pakete Module und Setup

#### Code 8: Einfaches Beispiel für eine setup.py Datei

```python
from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
)
```

### Lab 6.3: Optimale Organisation von großen Python-Projekten

#### Code 9: Grundlegende Projektstruktur

```plaintext
my_project/
│
├── my_package/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
│
├── tests/
│   ├── test_module1.py
│   └── test_module2.py
│
├── setup.py
└── README.md
```
