
# Python Schulung: Grundlagen der Websicherheit und Implementierung von Authentifizierung

## Einführung

In dieser Schulung konzentrieren wir uns auf die Grundlagen der Websicherheit und die Implementierung von Authentifizierung in Python-basierten Webanwendungen. Diese Themen sind essenziell, um sichere und robuste Webanwendungen zu entwickeln, die vor Angriffen geschützt sind und nur autorisierten Benutzern Zugang gewähren.

## Grundlagen der Websicherheit

### 1. SQL-Injection

SQL-Injection ist eine Angriffstechnik, bei der ein Angreifer bösartige SQL-Befehle in eine Abfrage einschleust, um unbefugten Zugriff auf die Datenbank zu erhalten.

**Beispiel einer unsicheren Abfrage:**

```python
# Unsichere Abfrage
username = input("Username: ")
query = f"SELECT * FROM users WHERE username = '{username}';"
```

**Sichere Abfrage mit vorbereiteten Statements:**

```python
import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

username = input("Username: ")
cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
```

### 2. Cross-Site Scripting (XSS)

XSS-Angriffe ermöglichen es Angreifern, bösartigen Code in Webseiten einzuschleusen, die von anderen Benutzern angesehen werden.

**Beispiel eines unsicheren Outputs:**

```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name", "")
    return f"<h1>Hallo, {name}!</h1>"
```

**Absicherung gegen XSS:**

Verwenden Sie HTML-Escape-Techniken oder Bibliotheken, die automatisch escapen.

### 3. Cross-Site Request Forgery (CSRF)

CSRF-Angriffe zielen darauf ab, eine authentifizierte Sitzung zu missbrauchen, indem ungewollte Aktionen im Namen des Benutzers ausgeführt werden.

**CSRF-Schutz in Flask:**

```python
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)
```

## Implementierung von Authentifizierung

### 1. Passwort-Hashing

Passwörter sollten niemals im Klartext gespeichert werden. Verwenden Sie stattdessen sichere Hashing-Algorithmen.

**Beispiel mit bcrypt:**

```python
import bcrypt

# Passwort hashen
password = b"supersecurepassword"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# Passwort-Überprüfung
if bcrypt.checkpw(password, hashed):
    print("Passwort korrekt")
else:
    print("Passwort falsch")
```

### 2. Implementierung von Login und Logout

Ein grundlegendes Authentifizierungssystem besteht aus Login- und Logout-Mechanismen.

**Beispiel mit Flask-Login:**

```python
from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin

app = Flask(__name__)
app.secret_key = 'your_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)

# Beispiel Benutzerklasse
class User(UserMixin):
    pass

@login_manager.user_loader
def user_loader(email):
    user = User()
    user.id = email
    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        user = User()
        user.id = email
        login_user(user)
        return redirect(url_for('protected'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out'

@app.route('/protected')
@login_required
def protected():
    return 'Logged in as: ' + request.form['email']

if __name__ == "__main__":
    app.run(debug=True)
```

## Fazit

Die Sicherheit von Webanwendungen ist ein kritischer Aspekt der Softwareentwicklung. Durch das Verständnis und die Implementierung von Sicherheitsmaßnahmen wie SQL-Injection-Schutz, XSS-Schutz und CSRF-Schutz sowie durch die Implementierung von Authentifizierungsmechanismen können Entwickler dazu beitragen, ihre Anwendungen sicherer zu machen.
