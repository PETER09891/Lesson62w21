def SeiveOfEratoshenes(num):
    prime = [True for i in range(num + 1)]
    p = 2

    while (p * p <= num):
        if prime[p] == True:
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1

    # Print only two-digit primes
    for p in range(10, min(num + 1, 100)):
        if prime[p]:
            print(p)

number = int(input("Enter a number: "))
print("Following are the two-digit prime numbers:")
SeiveOfEratoshenes(number)
