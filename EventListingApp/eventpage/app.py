from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

endpoint = "replace with your own endpoint"
port = 3306
dbname = "mydb"  # Updated database name
username = "admin"
password = "ADmin987"

def get_db_connection():
    return pymysql.connect(
        host=endpoint,
        user=username,
        password=password,
        database=dbname,
        port=port
    )

# index route to push list of events stored in MySQL
@app.route('/')
def index():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM event")
            events = cursor.fetchall()
    finally:
        connection.close()
    return render_template('index.html', events=events)


# add event route
@app.route('/add', methods=['POST'])
def add_event():
    name = request.form['name']
    date = request.form['date']
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO book (name, date) VALUES (%s, %s)", (name, date))
            connection.commit()
    finally:
        connection.close()
    return redirect(url_for('index'))

# delete event route
@app.route('/delete/<int:id>', methods=['POST'])
def delete_event(id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM event WHERE id = %s", (id,))
            connection.commit()
    finally:
        connection.close()
    return redirect(url_for('index'))


if __name__== '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')