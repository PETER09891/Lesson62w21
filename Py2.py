def SeiveOfEratoshenes(num):
    prime = [True for i in range(num + 1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, num):
        if prime[p]:
            print(p)

number = int(input("Enter a number: "))
print("Follwing are prime numbers smaller")
print("than or equal to", number) 
SeiveOfEratoshenes(number)      