# SQLite3 config

import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Check if the 'contacts' table already exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='contacts';")
table_exists = cursor.fetchone()

if not table_exists:
    cursor.execute('''
        CREATE TABLE contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            address TEXT,
            phone_number TEXT
        )
    ''')

conn.commit()
conn.close()


# Flask config

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        phone_number = request.form['phone_number']

        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO contacts (name, address, phone_number)
            VALUES (?, ?, ?)
        ''', (name, address, phone_number))

        conn.commit()
        conn.close()

        return redirect(url_for('success'))

    return '''
    <h2>Contact Form</h2>
    <form method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>

        <label for="address">Address:</label>
        <input type="text" id="address" name="address" required><br>

        <label for="phone_number">Phone Number:</label>
        <input type="text" id="phone_number" name="phone_number" required><br>

        <input type="submit" value="Submit">
    </form>
    <form action="/view" method="get">
        <input type="submit" value="View Form">
    </form>
    '''

@app.route('/success', methods=['GET', 'POST'])
def success():
    if request.method == 'POST':
        return redirect(url_for('index'))  # Redirect back to the form
    return 'Form submitted successfully!<br><form method="post"><input type="submit" value="Return to Form"></form>'

@app.route('/view', methods=['GET'])
def view():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM contacts')
    data = cursor.fetchall()

    conn.close()

    return render_template('view.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
