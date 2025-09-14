import mysql.connector
from geopy.distance import distance  # geodesic distance

DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "root",          # change if you use a non-root user
    "password": "9594",      # change to your password
    "database": "flight_game"
}

def fetch_coords(cur, icao: str):
    """
    Return (lat, lon, name) for given ICAO (ident) or None if not found/NULL coords.
    Assumes columns latitude_deg, longitude_deg, name in airport table.
    """
    cur.execute(
        """
        SELECT latitude_deg, longitude_deg, name
        FROM airport
        WHERE ident = %s
        """,
        (icao,)
    )
    row = cur.fetchone()
    if not row:
        return None
    lat, lon, name = row
    if lat is None or lon is None:
        return None
    return float(lat), float(lon), name

def main():
    icao1 = input("Enter first ICAO code: ").strip().upper()
    icao2 = input("Enter second ICAO code: ").strip().upper()

    if not icao1 or not icao2:
        print("Both ICAO codes are required.")
        return
    if icao1 == icao2:
        print("The ICAO codes are the same; distance is 0 km.")
        return

    conn = None
    cur = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cur = conn.cursor()

        a = fetch_coords(cur, icao1)
        b = fetch_coords(cur, icao2)

        missing = []
        if a is None:
            missing.append(icao1)
        if b is None:
            missing.append(icao2)
        if missing:
            print("Could not find coordinates for:", ", ".join(missing))
            print("Make sure the ICAO codes exist in the airport table (ident column).")
            return

        (lat1, lon1, name1) = a
        (lat2, lon2, name2) = b

        km = distance((lat1, lon1), (lat2, lon2)).km
        print(f"\nFrom {icao1} ({name1}) to {icao2} ({name2})")
        print(f"Distance: {km:.2f} km")

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        if cur is not None:
            try:
                cur.close()
            except Exception:
                pass
        if conn is not None and conn.is_connected():
            try:
                conn.close()
            except Exception:
                pass

if __name__ == "__main__":
    main()