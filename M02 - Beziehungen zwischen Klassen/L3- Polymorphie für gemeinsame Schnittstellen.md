
# Python Schulung: Polymorphie für gemeinsame Schnittstellen

## Einführung in Polymorphie

Polymorphie ist ein grundlegendes Konzept der objektorientierten Programmierung (OOP), das es ermöglicht, dass Objekte verschiedener Klassen auf dieselben Schnittstellen mit möglicherweise unterschiedlichen Implementierungen zugreifen können. In Python wird dies häufig durch den Einsatz von Vererbung und Methodenüberschreibung erreicht.

## Grundlagen der Polymorphie in Python

### Vererbung und Methodenüberschreibung

In Python können Klassen von anderen Klassen erben, was es ermöglicht, Methoden und Eigenschaften der Basisklasse zu nutzen oder zu überschreiben (override).

```python
class Bird:
    def fly(self):
        print("Some birds can fly.")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies at low altitudes.")

class Ostrich(Bird):
    def fly(self):
        print("Ostriches cannot fly.")
```

### Dynamisches Verhalten

Polymorphie ermöglicht es, das Verhalten von Objekten zur Laufzeit zu ändern, basierend darauf, von welcher Klasse ein Objekt instanziiert wird.

```python
def bird_flying_test(bird):
    bird.fly()

# Objekte erzeugen
sparrow = Sparrow()
ostrich = Ostrich()

# Polymorphes Verhalten testen
bird_flying_test(sparrow)  # Ausgabe: Sparrow flies at low altitudes.
bird_flying_test(ostrich)  # Ausgabe: Ostriches cannot fly.
```

## Praktische Anwendung

### Implementierung einer funktionalen Schnittstelle

Es ist nützlich, eine generische Schnittstelle zu definieren, die von verschiedenen Klassen implementiert wird. Dies ermöglicht eine flexible Codegestaltung, die viele spezifische Implementierungen unterstützen kann.

### Beispiel: Rechenoperationen

```python
class Operation:
    def execute(self, a, b):
        raise NotImplementedError("This method should be overridden by subclasses.")

class Add(Operation):
    def execute(self, a, b):
        return a + b

class Subtract(Operation):
    def execute(self, a, b):
        return a - b

def perform_operation(operation, a, b):
    return operation.execute(a, b)

# Beispiel
add_operation = Add()
print(perform_operation(add_operation, 5, 3))  # Ausgabe: 8
```

## Fazit

Polymorphie in Python bietet eine leistungsstarke Möglichkeit, flexiblen und wiederverwendbaren Code zu schreiben. Durch das Verstehen und Implementieren polymorpher Schnittstellen können Entwickler effizientere und dynamischere Anwendungen entwickeln.
