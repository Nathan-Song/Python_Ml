
# Einführung in die Webentwicklung mit Flask

## Was ist Flask?

Flask ist ein leichtgewichtiges Webframework für Python, das Entwicklern eine einfache und flexible Möglichkeit bietet, Webanwendungen zu erstellen. Es ist bekannt für seine Einfachheit und Modularität, wodurch es sich ideal für kleine bis mittelgroße Projekte eignet.

## Kernkonzepte

### Routing

Das Routing in Flask bestimmt, wie URLs auf Funktionen in Ihrer Anwendung abgebildet werden. Jede Route ist mit einer bestimmten Funktion verbunden, die ausgeführt wird, wenn die Route aufgerufen wird.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

### Templates

Templates ermöglichen es Ihnen, HTML-Inhalte dynamisch zu generieren. Flask verwendet Jinja2 als Template-Engine, die es erlaubt, Python-Ausdrücke in HTML einzubetten.

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
```

In der Datei `hello.html`:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Hello</title>
  </head>
  <body>
    <h1>Hello, {{ name }}!</h1>
  </body>
</html>
```

### Formulare und Anfragen

Flask bietet einfache Mittel, um Formulare zu verarbeiten und Daten zu empfangen, die von Benutzern eingegeben werden. Mit `request` können Sie auf Daten zugreifen, die über POST- oder GET-Anfragen gesendet wurden.

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        username = request.form['username']
        return f'Hello, {username}!'
    return '''
        <form method="post">
            Name: <input type="text" name="username">
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
```

## Praktische Anwendung

Eine praktische Anwendung in Flask könnte den Aufbau einer einfachen Blog-Plattform umfassen, bei der Benutzer Beiträge erstellen, lesen, aktualisieren und löschen können (CRUD-Operationen).

### Beispielprojekt: Mini-Blog

- Routen: Erstellung und Verwaltung von Blogbeiträgen
- Templates: Dynamische HTML-Seiten für das Blog-Frontend
- Formulare: Eingabeformulare für neue Beiträge

## Fazit

Flask ist ein hervorragendes Framework für Entwickler, die in die Webentwicklung mit Python einsteigen möchten. Es bietet eine ausgewogene Kombination aus Einfachheit und Leistungsfähigkeit und ist ideal für die Entwicklung sowohl einfacher als auch komplexer Webanwendungen.
