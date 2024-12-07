from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",            # MySQL host
        user="root",                 # MySQL username
        password="yagna1234",        # Replace with your MySQL root password
        database="dashboard_data"    # Database name
    )
    return conn

# Default route to display a welcome message
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Data API! Visit /data to view the dataset."

# Data endpoint to fetch insights
@app.route('/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM insights")  # Query to fetch all data
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)  # Convert result to JSON and return

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=50001, debug=True)
