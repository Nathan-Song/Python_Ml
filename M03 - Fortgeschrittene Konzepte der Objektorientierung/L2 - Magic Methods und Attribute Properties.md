
# Python Schulung: Magic Methods und Attribute Properties

## Einführung

Diese Schulung konzentriert sich auf zwei fortgeschrittene Python-Konzepte: Magic Methods und Attribute Properties. Beide Konzepte ermöglichen es Entwicklern, sauberen und effizienten Code zu schreiben, indem sie das Verhalten von Klassen und Instanzen anpassen.

## Magic Methods

Magic Methods sind spezielle Methoden, die mit doppelten Unterstrichen (z.B. `__init__`, `__str__`, `__repr__`) beginnen und in Python verwendet werden, um das Verhalten von Klassen zu modifizieren. Sie ermöglichen es uns, Operationen wie Vergleich, Addition, Längenprüfung und vieles mehr anzupassen.

### Beispiele

#### `__str__` und `__repr__`

Diese Methoden definieren, wie eine Klasse sich selbst als String darstellt, was besonders nützlich für Debugging-Zwecke ist.

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r})"
```

#### `__add__`

Diese Methode ermöglicht es Klasseninstanzen, mit dem `+` Operator addiert zu werden.

```python
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"
```

## Attribute Properties

Properties in Python sind eine saubere Art, Getter, Setter und Deleter in Klassen zu implementieren, wodurch die Verwaltung von Klassenattributen sicherer und intuitiver wird.

### Beispiel

```python
class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @full_name.setter
    def full_name(self, name):
        first_name, last_name = name.split()
        self._first_name = first_name
        self._last_name = last_name

    @full_name.deleter
    def full_name(self):
        print("Deleting name!")
        self._first_name = None
        self._last_name = None
```

## Zusammenfassung

Magic Methods und Attribute Properties sind kraftvolle Werkzeuge in Python, die helfen, den Code modular, wartbar und intuitiv zu gestalten. Diese Schulung soll Ihnen nicht nur das Verständnis dieser Konzepte vertiefen, sondern auch deren praktische Anwendung demonstrieren.

