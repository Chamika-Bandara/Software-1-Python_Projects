user_name_correct = "python"
password_correct = "rules"
attempt = 0

while attempt < 5:
    user_name = input("Enter user name: ")
    password = input("Enter password: ")

    if user_name == user_name_correct and password == password_correct:
        print("Welcome")
        break
    else:
        print(f"Enter correct user name and password again")
        if user_name != user_name_correct:
              print("You have entered the wrong user name")
        if password != password_correct:
            print(f"Enter have entered the wrong password")
        attempt += 1

if attempt == 5:
    print("Access denied")

