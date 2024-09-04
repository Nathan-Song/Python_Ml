
# Python Schulung

## Deskriptorklassen – Kontrollierter Zugriff auf Attribute und deren Einsatzmöglichkeiten

Deskriptoren in Python sind eine leistungsfähige Möglichkeit, den Zugriff auf Attribute einer Klasse zu kontrollieren. Sie ermöglichen die Implementierung von Logik, die jedes Mal ausgeführt wird, wenn ein Attribut abgerufen, gesetzt oder gelöscht wird.

## Kernkonzepte

### Was ist ein Deskriptor?

Ein Deskriptor ist ein Objektattribut mit „Bindungs“-Verhalten, das mindestens eine der Methoden `__get__`, `__set__` oder `__delete__` implementiert. Deskriptoren ermöglichen es, den Zugriff auf die Attribute von Klassen zu kontrollieren und zu verwalten.

```python
class Descriptor:
    def __get__(self, instance, owner):
        return f"Accessing the attribute from {owner.__name__}"

    def __set__(self, instance, value):
        raise AttributeError("Cannot modify this attribute")

    def __delete__(self, instance):
        raise AttributeError("Cannot delete this attribute")

class MyClass:
    attr = Descriptor()

obj = MyClass()
print(obj.attr)  # Ausgabe: Accessing the attribute from MyClass
obj.attr = 10    # Raise: AttributeError: Cannot modify this attribute
```

### Wie funktionieren Deskriptoren?

Deskriptoren werden in Python verwendet, um das Verhalten von Attributen auf Objekten zu steuern. Die Methoden `__get__`, `__set__`, und `__delete__` eines Deskriptors werden aufgerufen, wenn auf das Attribut zugegriffen wird, es gesetzt oder gelöscht wird.

- `__get__(self, instance, owner)`: Wird aufgerufen, um den Wert des Attributs abzurufen.
- `__set__(self, instance, value)`: Wird aufgerufen, um den Wert des Attributs zu setzen.
- `__delete__(self, instance)`: Wird aufgerufen, um das Attribut zu löschen.

### Praktische Einsatzmöglichkeiten

Deskriptoren können für verschiedene Zwecke verwendet werden:

1. **Validierung**: Überprüfen und Validieren von Daten vor dem Speichern in einem Attribut.
2. **Lazy Evaluation**: Verzögerte Berechnung und Speicherung eines Werts, wenn dieser zum ersten Mal abgerufen wird.
3. **Logging**: Protokollierung von Zugriffen auf ein Attribut, um Änderungen zu verfolgen.

### Beispiel: Validierung mit Deskriptoren

Ein häufiger Anwendungsfall für Deskriptoren ist die Validierung von Attributwerten.

```python
class PositiveNumber:
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value must be positive")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

class Account:
    balance = PositiveNumber()

    def __init__(self, initial_balance):
        self.balance = initial_balance

account = Account(100)
print(account.balance)  # Ausgabe: 100
account.balance = -50    # Raise: ValueError: Value must be positive
```

## Fazit

Deskriptorklassen bieten eine flexible und mächtige Möglichkeit, den Zugriff auf Attribute in Python-Klassen zu kontrollieren. Sie ermöglichen es Entwicklern, komplexe Logik für das Abrufen, Setzen und Löschen von Attributen zu implementieren und sind eine wertvolle Technik für die Implementierung von Mustern wie Validierung, Lazy Evaluation und Logging.
