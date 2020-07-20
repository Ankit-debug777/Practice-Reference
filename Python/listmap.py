#list comprehension 1 return sum of elements not including 8 and 9
def _sum(arr):
    l1 = list(map(int,str(arr)))
    print(l1)
    l1= [x for x in l1 if x != 8 if x!=9]
    print(l1)
    return(sum(l1))

arr = 2478989695
res = _sum(arr)
print(res)
