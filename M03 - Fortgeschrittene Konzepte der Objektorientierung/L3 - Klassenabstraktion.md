
# Python Schulung

## Klassenabstraktion – Wann und wie man abstrakte Klassen nutzt

Abstrakte Klassen in Python dienen als Vorlage für andere Klassen. Sie erlauben es, eine Struktur zu definieren, die Unterklassen implementieren müssen. Abstrakte Klassen werden mit dem `abc` Modul in Python erstellt und enthalten mindestens eine abstrakte Methode, die von den Unterklassen überschrieben werden muss.

## Wann sollte man abstrakte Klassen nutzen?

Abstrakte Klassen sind besonders nützlich, wenn:

- **Eine gemeinsame API** definiert werden soll, die alle Unterklassen implementieren müssen.
- **Vermeidung von Code-Duplikation** durch die Bereitstellung von gemeinsamen Funktionalitäten in der abstrakten Klasse.
- **Sicherstellen**, dass alle Unterklassen bestimmte Methoden implementieren, die in einer abstrakten Klasse definiert sind.

## Beispiel: Abstrakte Klasse für eine geometrische Form

```python
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
```

### Implementierung in Unterklassen

Hier ist ein Beispiel für die Implementierung der abstrakten Klasse `Shape`:

```python
class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius
```

### Verwendung der Klassen

```python
shapes = [Rectangle(3, 4), Circle(5)]

for shape in shapes:
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
```

## Vorteile der Verwendung von abstrakten Klassen

- **Klarheit und Struktur**: Es wird klar definiert, welche Methoden in den Unterklassen vorhanden sein müssen.
- **Ermöglicht Polymorphismus**: Objekte verschiedener Klassen können auf ähnliche Weise behandelt werden, wenn sie von derselben abstrakten Klasse abstammen.
- **Vermeidung von Fehlern**: Erzwingt die Implementierung wesentlicher Methoden in den Unterklassen.

## Praktische Anwendung

In der Praxis können abstrakte Klassen genutzt werden, um komplexe Systeme zu strukturieren, wie z.B. in der Entwicklung von Benutzeroberflächen, Spielmechaniken oder Datenverarbeitungssystemen, wo bestimmte Funktionalitäten in verschiedenen Kontexten konsistent umgesetzt werden müssen.

## Fazit

Abstrakte Klassen sind ein mächtiges Werkzeug in Python, um sauberen, gut strukturierten und wartbaren Code zu schreiben. Sie helfen dabei, eine klare Architektur in Ihren Projekten zu implementieren und die Einhaltung bestimmter Entwurfsmuster zu gewährleisten.
