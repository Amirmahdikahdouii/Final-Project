#Exercise-14
#Calculator
def calculator():
    """Check Function"""
    a,b,c = "","",""
    try:
        a = input("Please enter first number: ")
        a = float(a)
        c = input("Please Enter Character: ")
        if c.lower() == "end":
            exit(0)
        while c not in ["*", "/", "+", "-"] :
            """input again for character!"""
            print("Wrong Character!")
            c = input("Please Enter Character: ")
            if c.lower() == "end":
                exit(0)
        b = input("Please enter second Number: ")
        b = float(b)
        while True:
            if c == "*":
                print(a,c,b,"=",a*b)
                break
            elif c == "/":
                print(a,c,b,"=","%1.2f" %(a/b))
                break
            elif c == "+":
                print(a,c,b,"=",a+b)
                break
            elif c == "-":
                print(a,c,b,"=",a-b)
                break
    except:
        if str(a).lower() == "end":
            exit(0)
        if str(b).lower() == "end":
            exit(0)
        if str(c).lower() == "end":
            exit(0)
        print("please enter correct number!")
        calculator()

# print(calculator())





