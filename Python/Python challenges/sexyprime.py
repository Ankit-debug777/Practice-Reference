def isprime(n):
    list=[]
    for num in range(2,n+1):
        if num>1:
            for i in range(2,num//2+1):
                if num%i== 0:
                    break
            else:
                list.append(num)
    #print(list)

    for j in list:
        for k in list:
            if k-j == 6:
                print('(',j ,',', k ,')')

x = int(input('Enter a number'))
isprime(x)
