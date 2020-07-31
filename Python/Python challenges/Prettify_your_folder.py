'''Are your files unorganised?
prettify your directory
create a single function that takes inputs as path/location, dictionary file, and type of file
capitalize all the filenames
set a numeric naming convention for given type of file eg: for jpg --1.jpg 2.jpg ....'''

import os

def prettify(location,dictfile,typefile):
    #get list of files and folders in the location
    files =os.listdir(location)
    os.chdir(location)
    #read the dictionary file which contains names of files you do not want to change
    with open(dictfile) as fh:
        words = fh.read()
    for name in files:
        #name should not be in dictionary file and type should be file
        if name not in words and os.path.isfile(name):
            os.rename(name,name.capitalize())
    num=1
    for i in files:
        #chech type of file and if it matches then rename it
        try:
            if i.split(".")[1] == typefile:
                os.rename(i, f"{num}.{typefile}")
                num+=1
        except:
            continue

if __name__ == '__main__':
    print("Enter your choices: ")
    loc = input("Enter th path: ")
    print(os.listdir(loc))
    dictionaryfile = input("Enter your dictionary file: ")
    filetype = input("Enter the type of files you want to be renamed in numbered form: ")
    prettify(loc,dictionaryfile,filetype)
    print(os.listdir(loc))

