zander_size = int(input("Enter size of zander (cm): "))
if zander_size < 42:
    print("Release fish back in to the lake")
    print(f"The caught fish is {42-zander_size} cm below")
else:
    print("Zander fulfills the size limit")
