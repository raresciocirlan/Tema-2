from markupsafe import escape
import sqlite3
from flask import Flask, redirect, url_for, render_template, request, flash

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    teams = conn.execute('SELECT * FROM teams').fetchall()
    players = conn.execute('SELECT * FROM players').fetchall()
    conn.close()
    return render_template('index.html', teams=teams, players=players)

@app.route('/players/')
def play():
    conn = get_db_connection()
    players = conn.execute('SELECT * FROM players').fetchall()
    conn.close()
    return render_template('players.html', players=players)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        team = request.form['team']

        if not name:
            flash('Name is required!')
        elif not team:
            flash('Team is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO players (name, team) VALUES (?,?)',
                         (name, team))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/add/<int:n1>/<int:n2>/')
def add(n1, n2):
    return '<h1>{}</h1>'.format(n1 + n2)

@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))

@app.route('/about/')
def about():
    return '<h4>This is a Flask web application.</h4>'

if __name__ == '__main__':
    app.run()