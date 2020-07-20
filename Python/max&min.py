#find min and max from input
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        n = int(num)
        if largest == None:
            largest = n
            smallest = n
        elif largest < n:
            largest = n
        if smallest == None:
            smallest = n
        elif smallest > n:
            smallest = n
    except:
        print('Invalid input')
print('Maximum is', largest)
print('Minimum is', smallest)
