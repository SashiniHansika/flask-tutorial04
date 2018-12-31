from flask import Flask
from flask import render_template, request, redirect
import MySQLdb

app = Flask(__name__)

# MySql database configuration
conn = MySQLdb.connect(host="localhost",
                       user="root",
                       passwd="",
                       db="test123")
cur = conn.cursor()


@app.route('/', methods=['GET', 'POST'])
def display_home_page():
    return render_template('home.html')


@app.route('/register', methods=['POST', 'GET'])
def insert_user_details():

    if request.method == 'POST':
        first_name = request.form['fname']
        last_name = request.form['lname']
        email = request.form['email']
        contact_number = request.form['cnumber']
        password = request.form['pwd']

        if first_name and last_name and email and contact_number and password:

            cur.execute("INSERT INTO test123.users_details(First_name,Last_name,Email,Contact_number,Password)"
                " VALUES (%s, %s, %s, %s, %s)", (first_name, last_name, email, contact_number, password))
            conn.commit()
        return render_template('login.html')
    else:
        return render_template('register.html')


@app.route('/login', methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pwd']
        if email and password:
            cur.execute("SELECT First_name FROM test123.users_details where Email=%s and Password=%s", [email, password])
            data = cur.fetchall()
            print(data)
            return render_template('user_profile.html',data=data)
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run()
