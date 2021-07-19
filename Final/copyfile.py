#Exercise-34
class copy():
    def CopyFile(self):
        # global copy, a, b
        while True:
            # if file dosent exist,while loop can input again
            try:
                a = input("please enter source address: ")
                if a.lower() == "end":
                    exit(0)
                f = open(a, "r+b")
                copy = f.read()
                break
            except:
                if a.lower() == "end":
                    exit(0)
                print("oops file dosent found,please check your input and try again")
                continue

        while True:
            try:
                b = input("please enter destination address: ")
                if b.lower() == "end":
                    exit(0)
                paste = open (b,"w+b")
                paste.write(copy)
                print("Done!")
                break
            except :
                if b.lower() == "end":
                    exit(0)
                print("Address doesnt found!")
                continue