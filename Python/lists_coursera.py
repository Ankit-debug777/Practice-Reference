#count number of sender emails from txt file 
emaillist = list()
fname = input('Enter file name')
fh = open('mbox-short.txt')
for line in fh:
    if line.startswith('From '):
        words = line.split()
        emaillist.append(words[1])
        print(words[1])
print('there are', len(emaillist), 'lines having mail' )
