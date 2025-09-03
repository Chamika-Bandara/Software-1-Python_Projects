n = int (input("Enter an integer: "))

if n < 2:
    print("Not a prime number")
else:
    is_prime = True
    i = 2
    while i*i <=n:
        if n % i == 0:
            is_prime = False
            break
        i +=1
    print("Prime" if is_prime else "Not a prime number")
