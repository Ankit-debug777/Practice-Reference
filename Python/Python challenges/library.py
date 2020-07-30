# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book
# HarryLibrary = Library(listofbooks, library_name)

# dictionary (books-nameofperson)
# create a main function and run an infinite while loop asking
# users for their input
class Library:

    def __init__(self, books, lname):
        self.books = books
        self.name = lname

    @property
    def display(self):
        return self.books

    @property
    def dict(self):
        self.record={}
        return self.record

    @property
    def add(self):
        string = input("Which book do you want to add to the collection?\t")
        self.books.append(string)
        return f"{string} has been added to the collection"

    @property
    def lend(self):
        bname = input("Which book do you want? ")
        uname = input("Enter your Username: ")
        if bname in self.books:
            self.books.remove(bname)
            self.record[bname] = uname
            return f"Here you go {uname}. Take this {bname}"
        elif bname in self.record:
            return f"We're sorry. {self.record[bname]} has this book\nWe have many other books in our collection to choose from."
        else:
            return "\nMake sure you typed the book name correctly. Try again"

    @property
    def returnbook(self):
        bname = input("Which book do you want to return?\t ")
        self.record.pop(bname)
        self.books.append(bname)
        return f"Hope you enjoyed reading {bname}"

    def mylib(self):
        self.dict
        while True:
            print("\nWhat do you want to do?")
            print("1.Display books\t 2.Add book\t 3.Lend Book\t 4.Return book\t 0.Exit\n")
            choice = int(input())
            if choice == 0:
                break
            if choice==1:
                print(self.display)
            elif choice==2:
                print(self.add)
            elif choice==3:
                print(self.lend)
            elif choice==4:
                print(self.returnbook)

lib = Library([ 'The Lying Life of Adults','Hellfire','Transcendent Kingdom','The Glass Hotel','My Dark Vanessa',
                'The Death of Vivek Oji','Real Life','Wow, No Thank You.','Death in Her Hands'],"Central Library")
Library.mylib(lib)