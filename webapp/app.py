from flask import Flask, request
from db_config import db_config
import mysql.connector

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM user')
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


@app.route('/make_user', methods=['GET'])
def make():
    # http://127.0.0.1:5000/make_user?user=mike&email=mike@mail.com&pswd=mike
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    query = "INSERT INTO user (username,email,password) VALUES (%s, %s, %s)"
    values = (request.args["user"], request.args["email"], request.args["pswd"])
    try:
        cursor.execute(query, values)
        connection.commit()
    except mysql.connector.Error as e:
        print(e)
    cursor.close()
    connection.close()
    return request.args


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
