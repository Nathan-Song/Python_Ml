
# Python Schulung: Singleton Pattern

## Was ist das Singleton Pattern?

Das Singleton Pattern ist ein Entwurfsmuster, das sicherstellt, dass eine Klasse nur ein einziges Objekt erstellt und dass dieses Objekt global zugänglich ist. Es wird häufig verwendet, wenn nur eine Instanz einer Klasse benötigt wird, um den gesamten Systemstatus zu steuern.

## Implementierung des Singleton Patterns in Python

### Grundlegende Implementierung

Eine Möglichkeit, das Singleton Pattern in Python zu implementieren, besteht darin, den Konstruktor der Klasse so zu modifizieren, dass er bei jedem Aufruf die gleiche Instanz zurückgibt.

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance
```

### Beispielanwendung

Nachfolgend ein Beispiel, wie das Singleton Pattern verwendet wird, um sicherzustellen, dass nur ein einziges Objekt einer Klasse erstellt wird.

```python
class Logger(Singleton):
    def __init__(self):
        if not hasattr(self, 'log_file'):
            self.log_file = "logfile.txt"
            print(f"Log file created: {self.log_file}")

    def write_log(self, message):
        with open(self.log_file, 'a') as log:
            log.write(f"{message}
")

logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)  # Ausgabe: True
logger1.write_log("This is a log message.")
```

### Verwendung eines Decorators

Eine andere Möglichkeit, das Singleton Pattern zu implementieren, ist die Verwendung eines Decorators.

```python
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Logger:
    def __init__(self):
        self.log_file = "logfile.txt"
        print(f"Log file created: {self.log_file}")

    def write_log(self, message):
        with open(self.log_file, 'a') as log:
            log.write(f"{message}
")

logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)  # Ausgabe: True
logger1.write_log("This is another log message.")
```

## Praktische Anwendung

Das Singleton Pattern wird in vielen Anwendungen verwendet, bei denen eine einzige Instanz von Ressourcen benötigt wird, wie z.B.:

- **Logger**: Wie im obigen Beispiel gezeigt, ist es oft sinnvoll, eine einzige Instanz einer Logging-Klasse zu haben.
- **Datenbankverbindungen**: In großen Anwendungen kann eine zentrale Datenbankverbindung als Singleton implementiert werden.
- **Konfigurationen**: Anwendungskonfigurationen können zentral über eine Singleton-Klasse verwaltet werden.

## Fazit

Das Singleton Pattern ist ein nützliches Werkzeug, um sicherzustellen, dass bestimmte Klassen in einer Anwendung nur eine einzige Instanz haben. Durch seine Implementierung kann man sicherstellen, dass systemweite Ressourcen effizient genutzt und verwaltet werden.
