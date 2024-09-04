
# Python Schulung: Parallele Programmierung

## Einführung

Diese Schulung bietet eine Einführung in die parallele Programmierung mit Python. Der Schwerpunkt liegt auf den Techniken `Multiprocessing`, `Threading` und `Multiplexing`. Diese Techniken ermöglichen es, Aufgaben gleichzeitig auszuführen, um die Leistung von Anwendungen zu verbessern und die Ausführung von Programmen effizienter zu gestalten.

## Multiprocessing

### Was ist Multiprocessing?

Multiprocessing ermöglicht es, mehrere Prozesse gleichzeitig auszuführen, indem separate Prozesse für verschiedene Aufgaben erstellt werden. Jeder Prozess hat seinen eigenen Python-Interpreter und Speicherbereich, was bedeutet, dass sie unabhängig voneinander arbeiten können.

### Beispiel: Multiprocessing in Aktion

```python
import multiprocessing

def worker(num):
    # Funktion, die von jedem Prozess ausgeführt wird
    print(f'Worker: {num}')

if __name__ == '__main__':
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
```

## Threading

### Was ist Threading?

Threading ermöglicht es, mehrere Threads innerhalb desselben Prozesses gleichzeitig auszuführen. Im Gegensatz zu Prozessen teilen sich Threads den gleichen Speicherraum, was sie leichter, aber auch anfälliger für Race Conditions macht.

### Beispiel: Threading in Aktion

```python
import threading

def worker(num):
    # Funktion, die von jedem Thread ausgeführt wird
    print(f'Worker: {num}')

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

## Multiplexing

### Was ist Multiplexing?

Multiplexing erlaubt es einem Programm, auf mehrere Input/Output (I/O) Streams gleichzeitig zu reagieren. Dies ist besonders nützlich, wenn man mit vielen Netzwerkverbindungen oder anderen I/O-lastigen Aufgaben arbeitet.

### Beispiel: Multiplexing mit `select`

```python
import select
import socket

# Beispielhafte Sockets
sock1 = socket.socket()
sock2 = socket.socket()

# Einbinden in eine select-Abfrage
readable, writable, exceptional = select.select([sock1, sock2], [], [])

for s in readable:
    data = s.recv(1024)
    print(f'Daten empfangen: {data}')
```

## Praktische Anwendung

### Beispielprojekt: Web Crawler

- **Multiprocessing**: Aufteilen der Arbeit auf mehrere Prozesse, um Webseiten parallel zu durchsuchen.
- **Threading**: Verwenden von Threads, um die Seiten herunterzuladen, während andere verarbeitet werden.
- **Multiplexing**: Gleichzeitige Handhabung von Netzwerkverbindungen für eine schnelle und effiziente Datenübertragung.

## Fazit

Die parallele Programmierung in Python kann die Effizienz und Geschwindigkeit von Anwendungen erheblich verbessern. Durch das Verständnis und die Anwendung von `Multiprocessing`, `Threading` und `Multiplexing` können Entwickler komplexe und leistungsfähige Programme erstellen.
