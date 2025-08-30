while True:
    length = float(input("Enter the Length in inches:"))
    if length < 0:
        print("Program ended")
        break
    length_new = length * 2.54
    print(f"{length} inches = {length_new:.2f} cm")
