# myself Project
import Phone
import factorial
import exercise35


class Final:
    """Welcome"""

    def Exit(self):
        """ Exit Function"""
        return exit(0)

    def Fact(self):
        """factoral function
        #Exercise_3"""
        #Checked
        print("1.Factorial")
        while True:
            try:
                n = input("please enter your number: ")
                n = int(n)
                if n == 7:
                    try:
                        raise ValueError
                    except ValueError:
                        print("Number 7 has been pass!")
                        f = 1
                        for val in range(1, 4):
                            f *= val
                        print(f"3! = {f} ")
                        break
                while n <= 0:
                    n = input("please enter positive number: ")
                    n = int(n)
                f = 1
                for val in range(1, n+1):
                    f *= val
                print( f" {n}! = {f} ")
                break
            except:
                if str(n).lower() == "end":
                    return self.Exit()
                else:
                    print("please enter correct number!")
                    continue
        # ------------------------------

    def PhoneNumber(self):
        """Phone Number Modules should 
        import, 
        For More Information Read 
        \"Phone.py\"
        Class Programm"""
        print("2.Phone Number-(IRANCELL)")
        pre_numbers = ["0901","0902","0903","0904","0905"
        ,"0930","0933","0934","0935","0936","0937"
        ,"0938","0939"]
        shomare = ""
        while shomare not in pre_numbers:
            try:
                shomare = input("please enter your pre-number: ")
                shomare = int(shomare)               
                shomare = "0" + str(shomare)
            except:
                if shomare.lower() == "end":
                    return self.Exit()
                else:
                    print("please enter corrrect number!")
        address = input("Please enter your address: ")
        if address.lower() == "end":
            self.Exit()
        a = Phone.irancell_num(shomare, address).maker()
        return self.Starter()
        # ------------------------------

    def ReFactorial(self):
        """Recursive factorial 
        for Using This Programm Input should 
        be in range of (1-Num) """
        #Checked
        print("3.Recursive Factorial")
        while True:
            try:
                num = input("please Enter number: ")
                num = int(num)
                while num <= 0:
                    print("Please Enter possitive Number: ")
                    num = input("please Enter number: ")
                    num = int(num)
                break
            except:
                if str(num).lower() == "end":
                    self.Exit()
                else:
                    print("please Enter Correct Num: ")
                    continue
        example = factorial.fact(1, y=num)
        print(f"{num}! : {example}")
        # -------------------------------

    def FindWord(self):
        """Exercise-35
        found in File
        Free word-> Wrong Error"""
        #Checked
        print("4.Find Word")
        exercise35.a.Find()
        # --------------------------------

    def Decoder(self):
        """Exercise_2
           #Decorator"""
        #Checked
        print("5.Decorator")
        def My_Decorator(func):
            def Wrapper(a, b):
                if a > 0 and b > 0:
                    func(a, b)
                else:
                    print("Numbers Under Zero!")
            return Wrapper
        while True:
            val2 = val1 = 0
            try:
                while val1 < 1 :
                    val1 = input("please Enter First Number: ")
                    val1 = int(val1)
                while val2 < 1 :
                    val2 = input("please Enter Second Number: ")
                    val2 = int(val2)
                @My_Decorator
                def Division(a, b):
                    c = ("%1.2f" %(a/b))
                    print(f"{a}/{b} = {c}")
                Division(val1, val2)
                break
            except:
                if str(val1).lower() == "end":
                    return self.Exit()
                elif str(val2).lower() == "end":
                    return self.Exit()
                else:
                    print("Input Incorrect; please try again! ")
                    continue

        # ---------------------------------------------------------

    def Fibo(self):
        """Exercise_4
        Fibonacci"""
        print("6.Fibonacci")
        while True:
            try:
                a = input("please enter number: ")
                a = int(a)
                while a <= 1:
                    if a == 1:
                        print("1", "dosent exist fibonacci series")
                        a = input("please enter number: ")
                        a = int(a)
                    elif a <= 0:
                        a = input("please enter positive number: ")
                        a = int(a)
                break
            except:
                if str(a).lower() == "end":
                    exit(0)
                else:
                    print("please enter correct number! ")
                    continue
        # fibonacci series : 0,1,1,2,3,5,8,13,...
        n1 = 0
        n2 = 1
        while n1 <= a:
            n3 = n1+n2
            print(n1, end=" ")
            n1 = n2
            n2 = n3
        # ------------------------------
    def MinMax(self):
        """Min-Max Programm
        just with loop 
        with function we can perfome better,
        but I choose to Use Only Loop!"""
        #Checked
        print("7-Min-Max Numbers")
        while True:
            try:
                a = input("Please Enter Count Of Numbers: ")
                a = int(a)
                if a <= 0:
                    print("Number out Of Range!!")
                b = []
                Exit = None
                while a >= 1:
                    try:
                        c = input("please enter Number: ")
                        c = int(c)
                        if c > 50:
                            raise KeyError
                        b.append(c)
                        a -= 1
                        Exit = False
                    except KeyError:
                        print("Number bigger than 50!")
                        continue
                    except:
                        if str(c).lower() == "end":
                            Exit = "exit"
                            break
                        else:
                            print("please enter right Number ")
                            continue
                if Exit == "exit":
                    b = []
                    break
                elif Exit == True:
                    break
                elif Exit == False:
                    break
            except:
                if str(a).lower() == "end":
                    exit(0)
                else:
                    print("please enter right Number! ")
        # downer Try for handle IndexError
        # If Input will be >= 0 -->> we have IndexError in try
        try:
            max_number = b[0]
            min_number = b[0]
            for num in b:
                if num > max_number:
                    max_number = num
                if num < min_number:
                    min_number = num
            print('min-number is {} and max-number is {}'.format(min_number, max_number))
        except:
            exit(0)
    #------------------------------------

    def CopyFile(self):
        """Copy File"""
        #completly Checked
        print("8-CopyFile")
        import copyfile
        example = copyfile.copy().CopyFile()
    #------------------------------------
    
    def CapitaLetter (self):
        """Capital letter"""
        #completely Check
        print("9-Capital Letter")
        import CapitalLetter
        CapitalLetter.Captial()
    #------------------------------------

    def PrimeNumber(self):
        """Prime Number"""
        # Completely checked
        print("10.Prime Number")
        import primenumber
        primenumber.prime()
    #------------------------------------
    
    def Vowels (self):
        """Exercise-13
        Vowels sound
        """
        # Completely checked
        print("11.Vowels Sound")
        import Vowelsound
        Vowelsound.vowel()
    #------------------------------------
    
    def Calculator(self):
        """Exercise-14
        calculator
        """
        #completly Checked
        print("12.calculator")
        import Calculator
        print(Calculator.calculator())
    #------------------------------------

    def Waterbill(self):
        """Exercise-16
        """
        print("13.water bill")
        flag_Error_Count = True
        while flag_Error_Count == True:
            try:
                a = input("please enter count of homes: ")
                a = int(a)
                flag_Error_Count = False
            except:
                if a.lower() == "end":
                    exit(0)
                else:
                    print("please enter correct number!")
                    continue 
        d = {}
        key = 1
        while a > 0:
            try:
                val = input(f"please Enter persons of {key} homes: ")
                val = int(val)
                d[key] = val
                key += 1
                a -= 1
            except:
                if val.lower() == "end":
                    exit(0)
                else:
                    print("please enter correct number!")
                    continue

        flag_Error_bill = True
        while flag_Error_bill == True:
            try:
                billsome = input("please enter water bill price: ")
                billsome = int(billsome)
                flag_Error_bill = False
            except:
                if billsome.lower() == "end":
                    exit(0)
                else:
                    print("please enter correct number! ")
                    continue
                    
        persons = 0
        for val in d:
            persons += d[val]

        while True:
            c = billsome / persons
            print("amount for 1 person is %1.2f" %c)
            for val in d:
                e = d[val]*c
                print(val, "-> %1.2f" %e)
            else:
                break

    def Starter(self):
        """Starter Function
        for Receive input from User"""
        menu = """
        1.Fact
        2.Phone Number
        3.Recursive Factorial
        4.Find Word
        5.Decorator
        6.Fibonacci
        7.Min-Max Number
        8.Copy-File
        9.Capital-Letter
        10.Prime Number
        11.vowels
        12.Calculator
        13.water bill
        """
        print(menu)
        selector = input("please Enter your Choosing Number: ")
        if selector.lower() == "end":
            return self.Exit()
        elif selector == "1":
            return self.Fact()
        elif selector == "2":
            return self.PhoneNumber()
        elif selector == "3":
            return self.ReFactorial()
        elif selector == "4":
            return self.FindWord()
        elif selector == "5":
            return self.Decoder()
        elif selector == "6":
            return self.Fibo()
        elif selector == "7":
            return self.MinMax()
        elif selector == "8":
            return self.CopyFile()
        elif selector == "9":
            return self.CapitaLetter()
        elif selector == "10":
            return self.PrimeNumber()
        elif selector == "11":
            return self.Vowels()
        elif selector == "12":
            return self.Calculator()
        elif selector == "13":
            return self.Waterbill()
        else:
            print("please try again!")


a = Final()

while True:
    a.Starter()

