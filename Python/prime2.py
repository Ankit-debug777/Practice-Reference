upper = int(input('Upto what number?'))
def isprime(upper):
    for num in range(2, upper+1):
        for i in range(2, num//2+1):
            if (num % i) == 0:
                break
        else:
            print(num)
isprime(upper)
