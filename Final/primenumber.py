#prime Number
#Exercise 11
def prime():
    while True:
        try:
            number = input("Please Enter your Number: ")
            number = int(number)
            b = 0
            for val in  range (1,number+1):
                if number % val == 0 :
                    b+=1
            if b == 2:
                print("{} is a prime number".format(number))
                break
            else:
                print("{} is not a prime number".format(number))
        except:
            if str(number).lower() == "end":
                exit(0)
            else:
                print("please enter correct number! ")
                continue