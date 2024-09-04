
# Python Schulung

## Factory Pattern – Erzeugungsmuster für flexible und wiederverwendbare Objekte

Das Factory Pattern ist ein Erzeugungsmuster, das es ermöglicht, Objekte zu erstellen, ohne den genauen Klassennamen der zu erzeugenden Objekte angeben zu müssen. Dies fördert Flexibilität und Wiederverwendbarkeit im Code, insbesondere wenn verschiedene Objekte auf ähnliche Weise erzeugt werden müssen.

## Kernkonzepte

### Einführung in das Factory Pattern

Das Factory Pattern wird verwendet, um die Instanziierung von Objekten zu kapseln. Es ermöglicht eine flexiblere und dynamischere Erzeugung von Objekten, da der genaue Typ des Objekts zur Laufzeit bestimmt werden kann.

### Einfache Factory

Eine einfache Factory stellt eine Methode bereit, die basierend auf bestimmten Eingabedaten ein Objekt einer bestimmten Klasse zurückgibt.

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == 'dog':
            return Dog()
        elif animal_type == 'cat':
            return Cat()
        raise ValueError(f"Unknown animal type: {animal_type}")

# Nutzung der Factory
animal = AnimalFactory.create_animal('dog')
print(animal.speak())  # Ausgabe: Woof!
```

### Factory Method

Das Factory Method Pattern ist eine erweiterte Form des Factory Patterns, bei dem die Erstellung der Objekte durch Subklassen dynamisch verändert werden kann.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

# Nutzung der Factory Method
factory = DogFactory()
dog = factory.create_animal()
print(dog.speak())  # Ausgabe: Woof!
```

## Praktische Anwendung

In der Praxis wird das Factory Pattern häufig in großen Softwareprojekten verwendet, bei denen viele ähnliche Objekte erstellt werden müssen. Es wird auch verwendet, um die Kopplung zwischen Klassen zu reduzieren, was den Code wartbarer und erweiterbarer macht.

### Beispielprojekt: Fahrzeugproduktion

- Ein Fahrzeugproduktionssystem, bei dem verschiedene Fahrzeugtypen (z.B. Auto, LKW, Motorrad) durch eine zentrale Factory erstellt werden können.
- Die Factory kann erweitert werden, um neue Fahrzeugtypen zu unterstützen, ohne bestehende Codebasis zu verändern.

## Fazit

Das Factory Pattern ist ein grundlegendes Designmuster, das Entwicklern hilft, flexiblen und wiederverwendbaren Code zu schreiben. Durch die Implementierung dieses Musters können Entwickler den Instanziierungsprozess von Objekten vereinfachen und gleichzeitig die Codebasis besser organisieren.
