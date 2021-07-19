# a = [1,2,3,4,-1,5,14,88,90,32,15,70,-20,2.5,3.1,9.05,45,66,66.6,3345,0.5]
# max_number = a[0]
# min_number = a[0]
# for num in a :
#      if num > max_number :
#         max_number = num
#      if num < min_number :
#         min_number = num
# print ('min-number is {} and max-number is {}'.format(min_number,max_number))

# #min=Max
# #Exercise_10
# while True:
#     try:
#         a = input("How many Items Do you Want to Input? ")
#         a = int(a)+1
#         b = []
#         for val in range(1,a):
#             print(f"please Enter {val}.st Numbers: ", end ="")
#             try:
#                 c = input()
#                 c = int(c)
#                 b += c
#             except:
#                 if str(c).lower() == "end":
#                     exit(0)
#                 else:
#                     print("please enter correct number!")
                    
#     except:
#         if str(a).lower() == "end":
#             exit(0)
#         else:
#             print("Please Enter Number!")
#             continue