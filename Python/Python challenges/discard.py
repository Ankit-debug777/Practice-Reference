#import this
lst1= [14,27,1,4,2,50,3,1]
lst2=[2,4,-4,3,1,1,14,27,50]
#discard an odd character from one of the list 
def discard(lst1,lst2):
    dis = []
    if len(lst1) > len(lst2):
        dis = ([x for x in lst1 if x not in lst2])
    elif len(lst2) > len(lst1):
        dis = ([y for y in lst2 if y not in lst1])
    return dis[0]
print(discard(lst1,lst2))

def setmethod(lst1,lst2):
    return
