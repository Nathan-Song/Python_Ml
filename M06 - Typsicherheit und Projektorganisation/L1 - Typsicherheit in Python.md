
# Python Schulung: Typsicherheit in Python

## Was ist Typsicherheit?

Typsicherheit in Python bezieht sich auf die Praxis, Datentypen explizit anzugeben und sicherzustellen, dass Variablen nur Werte eines bestimmten Typs enthalten. Dies kann zur Verbesserung der Codequalität und zur Reduzierung von Laufzeitfehlern beitragen. Während Python dynamisch typisiert ist, ermöglicht die Einführung von Typannotationen in Python 3 eine bessere Unterstützung der Typsicherheit.

## Typannotationen

Typannotationen in Python ermöglichen es, den erwarteten Typ von Variablen, Funktionsparametern und Rückgabewerten anzugeben.

### Beispiel: Typannotationen in Funktionen

```python
def add_numbers(a: int, b: int) -> int:
    return a + b

result: int = add_numbers(5, 3)
```

In diesem Beispiel wird angegeben, dass die Funktion `add_numbers` zwei Parameter `a` und `b` vom Typ `int` erwartet und ebenfalls einen `int` zurückgibt.

### Typannotationen für Variablen

Auch Variablen können mit Typannotationen versehen werden, um ihre erwarteten Typen zu kennzeichnen.

```python
name: str = "Alice"
age: int = 30
```

## Vorteile der Typsicherheit

- **Früherkennung von Fehlern**: Typfehler können bereits während der Entwicklung und nicht erst zur Laufzeit entdeckt werden.
- **Verbesserte Lesbarkeit**: Der Code wird für andere Entwickler verständlicher, da die erwarteten Datentypen klar dokumentiert sind.
- **Bessere IDE-Unterstützung**: Moderne IDEs und Editoren können Typannotationen nutzen, um besseren Code-Vervollständigung und Fehlererkennung zu bieten.

## Praktische Anwendung

### Beispielprojekt: Einfache Benutzerverwaltung

Eine einfache Benutzerverwaltung könnte durch die Einführung von Typannotationen robuster gestaltet werden.

```python
from typing import List

class User:
    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email

def add_user(users: List[User], new_user: User) -> List[User]:
    users.append(new_user)
    return users

users: List[User] = []
new_user = User("john_doe", "john@example.com")
users = add_user(users, new_user)
```

In diesem Beispiel verwenden wir Typannotationen, um sicherzustellen, dass die Liste `users` nur `User`-Objekte enthält und dass die Funktion `add_user` eine Liste von `User`-Objekten zurückgibt.

## Typprüfung mit mypy

Mypy ist ein Tool, das statische Typprüfungen in Python ermöglicht. Es kann verwendet werden, um den Code auf Typfehler zu überprüfen.

### Installation und Verwendung von mypy

1. Installation:
    ```bash
    pip install mypy
    ```

2. Überprüfung des Codes:
    ```bash
    mypy script.py
    ```

Mypy durchsucht den Code nach Typverletzungen und zeigt potenzielle Probleme an.

## Fazit

Die Typsicherheit in Python ermöglicht es Entwicklern, robusteren und leichter wartbaren Code zu schreiben. Durch die Verwendung von Typannotationen und Tools wie mypy können potenzielle Fehler frühzeitig erkannt und behoben werden.
