nums = []
while True:
    s = input ("Enter a number (empty to quit): ")
    if s =="":
        break
    try:
        nums.append(float(s))
    except ValueError:
        print("Invalid input try again")

if nums:
    nums.sort(reverse=True)
    top5 = nums[:5]
    print(f"The top 5 numbers (in descending order) are: {top5}")
else:
    print("No numbers were entered")