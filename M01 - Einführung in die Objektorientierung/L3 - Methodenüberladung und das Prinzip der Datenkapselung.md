
# Python Schulung: Methodenüberladung und Datenkapselung

## Methodenüberladung

In Python gibt es keine native Unterstützung für Methodenüberladung wie in einigen anderen Programmiersprachen. Stattdessen kann Methodenüberladung durch verschiedene Techniken simuliert werden, wie die Verwendung von Standardargumenten oder die `*args` und `**kwargs` Parameter.

### Beispiel: Methodenüberladung durch Standardargumente

```python
def add(a, b, c=0):
    return a + b + c

# Aufrufe der Methode mit unterschiedlichen Argumenten
print(add(2, 3))     # Ausgabe: 5
print(add(2, 3, 4))  # Ausgabe: 9
```

### Beispiel: Methodenüberladung mit `*args`

```python
def add(*args):
    return sum(args)

# Unterstützt eine beliebige Anzahl von Argumenten
print(add(1, 2, 3))      # Ausgabe: 6
print(add(1, 2, 3, 4, 5)) # Ausgabe: 15
```

## Datenkapselung

Datenkapselung in Python bezieht sich auf den Einschluss von Variablen und Methoden innerhalb einer Klasse und die Beschränkung des Zugangs zu diesen, um eine sichere Manipulation der Daten zu gewährleisten.

### Beispiel: Verwendung von privaten Attributen

```python
class Account:
    def __init__(self, owner, amount):
        self.owner = owner
        self.__amount = amount  # Privates Attribut

    def deposit(self, amount):
        if amount > 0:
            self.__amount += amount
            print("Deposit Successful")
        else:
            print("Invalid Amount")

    def show_balance(self):
        print(f"Current Balance: {self.__amount}")

acc = Account('John Doe', 1000)
acc.deposit(500)
acc.show_balance()  # Current Balance: 1500
```

## Fazit

Methodenüberladung und Datenkapselung sind wichtige Konzepte in der Programmierung, die in Python durch verschiedene Techniken umgesetzt werden können. Die Kenntnis dieser Konzepte und Techniken ermöglicht es Entwicklern, flexiblere und sicherere Programme zu erstellen.
