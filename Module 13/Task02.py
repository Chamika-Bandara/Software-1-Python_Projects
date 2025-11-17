import json

import mysql.connector
from flask import Flask

app = Flask (__name__)
app.json.sort_keys = False

connection = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="9594",
            database="flight_game"
        )

@app.route("/airport/<icao>")
def airport(icao):
        sql = f'select name, municipality from airport where ident = {icao}'
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            name, town = result
            response = {
                "ICAO": icao,
                "NAme": name,
                "Location": town,
            }
            return response
        else:
            response = json.dumps({"message":"No airport found with that ICAO code"})
            return Response(response=response, status=404, mimetype='application/json')

if __name__ == "__main__":
    app.run(debug=True, host = "127.0.0.1", port = 5001)