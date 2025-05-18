from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection

#Home Page
@app.route('/')
def index():
    connection = get_db_connection()
    clients = connection.execute('SELECT * FROM clients').fetchall()
    connection.close()
    return render_template('index.html', clients=clients)

@app.route('/add_client', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        phone = request.form['phone']
        frequency = request.form['frequency']

        connection = get_db_connection()
        connection.execute('INSERT INTO clients (name, address, phone, frequency) VALUES (?, ?, ?, ?)', name, address, phone, frequency)
        connection.commit()
        connection.close()
        return redirect(url_for('index'))
    return render_template('add_client.html')


if __name__ == '__main__':
    app.run(debug=True)