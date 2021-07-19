#exercise-32
class ValueNotFound(Exception):
    """ class for raising error if input
    dosent exist"""
    pass
class irancell_num (ValueNotFound):
    def __init__(self,num,Address):
        self.num =num
        # nums = for check to understand input is correct or No.
        nums =["0901","0902","0903","0904","0905"
        ,"0930","0933","0934","0935","0936","0937"
        ,"0938","0939"]
        self.nums = nums
        self.address = Address
    def maker (self):
        try:
            with open(str(self.address),"w") as f:
                #for clearing the text if is exist
                f.close()
            for val in range(1000000,1000005):
                with open(str(self.address),"a") as f:
                    f.write(str(self.num))
                    f.write(str(val))
                    f.write("\n")
                    if str(val) == "1000004":
                        f.write("The End")
        except:
            print("your address doesnt found!")
 

     


#Example
# a = irancell_num("0930","H:\hxt.txt").maker()