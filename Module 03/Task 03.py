biological_gender = input("Enter your Biological Gender (Male/Female): ").strip().lower()
hemoglobin_value = float(input("Enter your hemoglobin value (g/l): "))
if biological_gender == "male":
    if 134 <= hemoglobin_value <= 167 :
        print("Your hemoglobin value is normal")
    elif hemoglobin_value < 134 :
        print("Your hemoglobin value is low!!!")
    else:
        print("Your hemoglobin value is high!!!")
elif biological_gender == "female":
    if 117 <= hemoglobin_value <= 155 :
        print("Your hemoglobin value is normal")
    elif hemoglobin_value < 117:
        print("Your hemoglobin value is low!!!")
    else:
        print("Your hemoglobin value is high!!!")