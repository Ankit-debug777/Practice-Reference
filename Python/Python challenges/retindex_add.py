#given the inputs(lst,t) return indexes [x,y] such that addition of elements from index x to index y should be equal to t
def ans(lst,t):
    sum = 0
    for x in range(len(lst)):
        for y in range(len(lst)):
            if x>y: continue
            sum = sum + lst[y]
            if sum ==t:
                print([x,y])
                quit()
        else:
            sum = 0
    else:
        print([-1,-1])
#example input
ans([4,3,10,2,8],20)
