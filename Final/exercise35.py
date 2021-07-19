#Exercise_35
class WrongError (Exception):
    pass
class Check (WrongError):
    def Find(self):
        a = input("please Enter Your File Address: ")
        b = ""
        if a.lower() == "end":
            return exit(0)
        try:
            with open (a) as f:
                l = f.readlines()
            Freecount = 0
            b = input("please Enter Your Word That You looking For: ")
            if b.lower() == "end":
                exit(0)
            wordCount = 0
            for val in l :
                if "free" in val.lower():
                    Freecount += val.count("free")
                if b in val :

                    wordCount += val.count(b)
            print ("----------------------------")
            print (f" {b} in Text: {wordCount} Times!")
            try:
                if Freecount > 0 :
                    raise WrongError 
            except WrongError as WR:
                print (f""" WrongWord Error    
---------------------------            
We Have Found \'Free\' 
in your File {Freecount} Times!
---------------------------""")
        except:
            if b.lower() == "end":
                exit(0)
            print("Oops file Doesnt Found, please Try Again")
            self.Find()


a= Check()
# a.Find()