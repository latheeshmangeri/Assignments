import datetime

from flask import Flask, render_template, request
import pymysql
from werkzeug.utils import redirect

app = Flask(__name__)


# Initialize MySQL
mysql = pymysql.connect(
    host="academicmysql.mysql.database.azure.com",
    user="lxm6009",
    password="Lathi2525@",
    database="lxm6009"
)

@app.route('/')
def index():
    # Retrieve data from MySQL
    with mysql.cursor() as cursor:
        cursor.execute('SELECT * FROM Customers')
        data = cursor.fetchall()
        # Get data from the form
    date_str = request.form['date']
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')  # Assuming the form input is in YYYY-MM-DD format

    # Insert data into MySQL
    with mysql.cursor() as cursor:
        cursor.execute('INSERT INTO your_table_name (date_column) VALUES (%s)', (date_obj,))
        mysql.commit()

    return render_template('index.html', data=data)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Get data from the form
        date_str = request.form['date']
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')  # Assuming the form input is in YYYY-MM-DD format

        # Insert data into MySQL
        with mysql.cursor() as cursor:
            cursor.execute('INSERT INTO your_table_name (date_column) VALUES (%s)', (date_obj,))
            mysql.commit()

        return redirect('/')

    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)
