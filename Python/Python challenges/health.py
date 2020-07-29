def getdate():
    import datetime
    return datetime.datetime.now()

def entry(name,mode):
    if name.lower() == "rohan":
        if mode == "1":
            with open("rohanex.txt", "a+") as fh:
                line = input("What exercises did you perform\n")
                fh.write("\n")
                fh.write(str(getdate()))
                fh.write("-")
                fh.write(line)

        elif mode == "2":
            with open("rohandiet.txt", "a+") as fh:
                line = input("What did you eat?\n")
                fh.write("\n")
                fh.write("-")
                fh.write(str(getdate()))
                fh.write(line)

    if name.lower() == "harry":
        if mode == "1":
            with open("harryex.txt", "a+") as fh:
                line = input("What exercises did you perform\n")
                fh.write("\n")
                fh.write(str(getdate()))
                fh.write("-")
                fh.write(line)

        elif mode == "2":
            with open("harrydiet.txt", "a+") as fh:
                line = input("What did you eat?\n")
                fh.write("\n")
                fh.write(str(getdate()))
                fh.write("-")
                fh.write(line)

    elif name.lower() == "hammad":
        if mode == "1":
            with open("hammadex.txt", "a+") as fh:
                line = input("What exercises did you perform\n")
                fh.write("\n")
                fh.write(str(getdate()))
                fh.write("-")
                fh.write(line)

        elif mode == "2":
            with open("hammaddiet.txt", "a+") as fh:
                line = input("What did you eat?\n")
                fh.write("\n")
                fh.write(str(getdate()))
                fh.write("-")
                fh.write(line)


def retrieve(name,mode):
    if name.lower() == "rohan":
        if mode == "1":
            fh= open("rohanex.txt")
            lines = fh.readlines()
            print(lines)
        elif mode == "2":
            with open("rohandiet.txt") as fh:
                lines = fh.readlines()
                print(lines)
    if name.lower() == "harry":
        if mode == "1":
            with open("harryex.txt") as fh:
                lines = fh.readlines()
                print(lines)
        elif mode == "2":
            with open("harrydiet.txt") as fh:
                lines = fh.readlines()
                print(lines)
    if name.lower() == "hammad":
        if mode == "1":
            with open("hammadex.txt") as fh:
                lines = fh.readlines()
                print(lines)
        elif mode == "2":
            with open("hammaddiet.txt") as fh:
                lines = fh.readlines()
                print(lines)


activity = input("Do you want to log[1] or retrieve data[2] :")
name = input("Which client do you want to access: Harry, Rohan or Hammad\n")
mode = input("Select exercise[1] or  diet[2]: ")
if activity == "1":
    entry(name,mode)
if activity == "2":
    retrieve(name, mode)
