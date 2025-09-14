import mysql.connector
def main():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="9594",
            database="flight_game"
        )

        cursor = connection.cursor()

        icao = input("Enter ICAO code: ").strip().upper()

        query = """
            select name, municipality
            from airport
            where ident = %s
        """
        cursor.execute(query, (icao,))
        result = cursor.fetchone()

        if result:
            print(f"Airport name: {result[0]}")
            print(f"Location (town): {result[1]}")
        else:
            print("No Airport found with that ICAO code.")

    except mysql.connector.Error as error:
        print(f"Error: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    main()