airports = {}

while True:
    print("\nOptions:")
    print("1= Enter a new Airport")
    print("2= Fetch Airport information")
    print("3= Quit")

    choice = input("Choose an option(1-3): ")

    if choice == "1":
        icao = input("Enter ICAO code: ").upper()
        name = input("Enter Airport Name: ")
        airports[icao] = name
        print(f"Airport {name} with ICAO code {icao} is added.")

    elif choice == "2":
        icao = input("Enter ICAO code: ").upper()
        if icao in airports:
            print(f"Airport Name: {airports[icao]}")
        else:
            print("No Airport not found with that ICAO code.")

    elif choice == "3":
        print("Exiting program. Goodbye!!")
        break

    else:
        print("Invalid choice, please enter 1,2 or 3.")

