
# Python Code Examples from Presentation - Day 3

## Modul 7: Debugging und Optimierung

### Debugging Techniken – Effektive Fehlersuche in Python-Projekten

#### Code 1: Einfache Debugging-Technik mit pdb

```python
import pdb

def fehlerhafte_funktion(a, b):
    pdb.set_trace()  # Debugging startet hier
    result = a / b
    return result

# Beispielhafte Nutzung:
fehlerhafte_funktion(10, 0)
```

### Logging in Python – Protokollierung und Nachvollziehbarkeit von Programmabläufen

#### Code 2: Einfache Protokollierung mit dem logging-Modul

```python
import logging

# Konfiguration des Loggings
logging.basicConfig(filename='app.log', level=logging.INFO)

def division(a, b):
    try:
        result = a / b
        logging.info(f"Division erfolgreich: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logging.error("Division durch Null versucht")
        return None

# Beispielhafte Nutzung:
division(10, 2)
division(10, 0)
```

### Laufzeitanalyse und Optimierung – Performance analysieren und verbessern

#### Code 3: Nutzung von timeit zur Laufzeitanalyse

```python
import timeit

code = '''
def summiere_bis_n(n):
    return sum(range(n))

summiere_bis_n(1000000)
'''

# Zeitmessung
laufzeit = timeit.timeit(code, number=100)
print(f"Laufzeit: {laufzeit} Sekunden")
```

## Modul 8: Webentwicklung mit Python

### Flask – Ein leichtgewichtiges Webframework – Einführung in die Webentwicklung mit Flask

#### Code 4: Einfacher Flask-Server

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Willkommen bei Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

### REST APIs erstellen – Aufbau und Implementierung von RESTful APIs mit Flask

#### Code 5: Einfache RESTful API mit Flask

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/summe', methods=['POST'])
def summe():
    daten = request.get_json()
    result = sum(daten['zahlen'])
    return jsonify({'summe': result})

if __name__ == '__main__':
    app.run(debug=True)
```

### Sicherheit und Authentifizierung – Grundlagen der Websicherheit und Implementierung von Authentifizierung

#### Code 6: Einfaches Authentifizierungssystem mit Flask

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

users = {"admin": "passwort"}

@app.route('/login', methods=['POST'])
def login():
    daten = request.get_json()
    username = daten.get('username')
    password = daten.get('password')

    if users.get(username) == password:
        return jsonify({"message": "Login erfolgreich"}), 200
    else:
        return jsonify({"message": "Login fehlgeschlagen"}), 401

if __name__ == '__main__':
    app.run(debug=True)
```

## Modul 9: Grafische und parallele Programmierung

### Grafische Programmierung mit Tkinter – GUI-Anwendungen in Python erstellen

#### Code 7: Einfaches Tkinter-Fenster

```python
import tkinter as tk

def on_button_click():
    print("Button wurde geklickt")

root = tk.Tk()
root.title("Einfaches Tkinter-Fenster")

button = tk.Button(root, text="Klick mich", command=on_button_click)
button.pack()

root.mainloop()
```

### Parallele Programmierung – Einführung in Multiprocessing, Threading und Multiplexing

#### Code 8: Einfache Multiprocessing-Beispiel

```python
import multiprocessing

def worker(num):
    print(f'Worker: {num}')

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
```

### Simulation und Modellierung – Komplexe Systeme parallel simulieren

#### Code 9: Simulation mit Threads

```python
import threading
import time

def simulate(task_name, delay):
    print(f"{task_name} startet")
    time.sleep(delay)
    print(f"{task_name} abgeschlossen")

threads = []

tasks = [("Aufgabe 1", 2), ("Aufgabe 2", 3), ("Aufgabe 3", 1)]

for task_name, delay in tasks:
    t = threading.Thread(target=simulate, args=(task_name, delay))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Alle Aufgaben abgeschlossen")
```

# Weitere Beispiele könnten in einem ähnlichen Format hinzugefügt werden.
