#coursera X-Dspam-Confidence
fname = input('Enter a file name: ')
fhand = open(fname)
count = 0
tot = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        ipos = line.find(':')
        num = line[ipos+2:]
        fnum = float(num)
        tot = tot + fnum
        count = count + 1
#print(found)
#print(count)
print('Average Spam Confidence:',tot/count)
