import mysql.connector
def main():
    global connection, connection
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="9594",
            database="flight_game"
        )

        cursor = connection.cursor()

        iso_code = input("Enter ISO Country/area code:").strip().upper()
        query = """
            select type, count(*)
            from airport
            where iso_country = %s
            group by type
            order by type;
            """
        cursor.execute(query,(iso_code,))
        results = cursor.fetchall()

        if not results:
            print(f"No airports found for {iso_code}")
        else:
            print(f"\nAirports in {iso_code} by type:\n")
        for airport_type, count in results:
            print(f"{airport_type}: {count}")

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    main()

