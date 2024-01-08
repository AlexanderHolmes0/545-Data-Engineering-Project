from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os.path
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    "host": "mysql-33ef51dc-vols-84b2.aivencloud.com",
    "user": "api_user",
    "password": "REDACTED",
    "database": "defaultdb",
    "port": "23825",
}


def create_connection():
    return mysql.connector.connect(**db_config)


@app.route("/get_data", methods=["GET"])
def get_data():
    try:
        conn = create_connection()
        cursor = conn.cursor()

        # Execute a query to retrieve data
        cursor.execute("SELECT * FROM Feature_Store ORDER BY RAND() LIMIT 10")

        # Fetch the results
        data = cursor.fetchall()

        conn.close()

        # Format the data as needed and return it as JSON
        response = [
            {
                "index": row[0],
                "salesdate": row[1],
                "productid": row[2],
                "region": row[3],
                "freeship": row[4],
                "discount": row[5],
                "itemssold": row[6],
                "error_code": row[7],
            }
            for row in data
        ]

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
