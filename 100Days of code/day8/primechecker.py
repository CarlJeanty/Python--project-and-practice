def prime_checker(n):
    isprime = True
    for i in range(2,n):
        if n%1 ==0:
            isprime = False
    if isprime ==True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")



n = int(input("Enter a whole number"))
prime_checker(n)