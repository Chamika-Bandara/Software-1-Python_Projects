Lots_in_Pound = 32
Pounds_in_Talent = 20
Grams_in_Lot = 13.3

talents = float(input("Enter your talents:\n "))
Pounds = float(input("Enter your Pounds:\n "))
Lots = float(input("Enter your Grams:\n "))

total_lots = (talents * Pounds_in_Talent * Lots_in_Pound) + (Pounds * Lots_in_Pound) + Lots

total_grams = total_lots * Grams_in_Lot

kilograms = int(total_grams// 1000)
grams = total_grams % 1000

print("\nThe weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")