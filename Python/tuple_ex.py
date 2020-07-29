#coursera tuple exercise
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
stat = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        tim = words[5].split(':')
        hrs = tim[0]
        stat[hrs] = stat.get(hrs,0) + 1 #dict add hours and their count
print(stat)
#add dict items to list with key-val as tuples
lst = list()
for h,c in stat.items():
    tmp = (h,c)
    lst.append(tmp)
#sort list
lst = sorted(lst, reverse = False)
for h,c in lst:
    print(h,c)
