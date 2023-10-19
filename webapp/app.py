from flask import Flask
import mysql.connector

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    config = {
        'user': 'root',
        'password': 'G7ue4$4/e6',
        'host': '127.0.0.1',
        'port': '3306',
        'database': 'sales'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM k_contract')
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    for item in results:
        print(item)
    return "okay, im here\n"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
