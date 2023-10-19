from flask import Flask
import mysql.connector

app = Flask(__name__)
db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'sales'
}


@app.route('/', methods=['GET'])
def index():
    connection = mysql.connector.connect(**db_config)
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
