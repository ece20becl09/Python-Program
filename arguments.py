# # def p1(*args):
# #     sum=0
# #     print ("calling the function")
# #     for i in args:
# #         sum=sum+i
# #         print (sum)
# # a=int(input("Eter the input1\n"))
# # b=int(input("Enter the input2\n"))
# # c=int(input("Enter the input3\n"))
# # p1(a,b,c,80)
#
# # try:
# #     a=int(input("Enter the input1\n"))
# # except Exception as y:
# #     print ("First inout is wrong and errr is {0}".format(y))
# # try:
# #     b=int(input("enter second input1\n"))
# # except Exception as e:
# #     print ("Secod input is wrong and error is {0}".format(e))
# # #c=int(input("eneyet he input3\n"))
# # try:
# #     print ("Try block is success")
# #     c=a+b
# #     print (c)
# # except:
# #     print ("Both inputs or single input is not digit")
# # print ("==========================================")
# # h=int(input("enete the nput\n"))
# # kl=h+50
# # print(kl)
#
#
# try:
#     a=int(input("Enter the input1\n"))
# except Exception as y:
#     print ("First inout is wrong and errr is {0}".format(y))
#     a = int(input("Giving another chanceEnter the input1\n"))
# try:
#     b=int(input("enter second input2\n"))
# except Exception as e:
#     print ("Secod input is wrong and error is {0}".format(e))
#     try:
#         b = int(input("Giving another chance enter second input2\n"))
#     except:
#         print ("Seocnd chancbe also failed")
# #c=int(input("eneyet he input3\n"))
# try:
#     print ("Try block is success")
#     c=a+b
#     print (c)
# except:
#     print ("Both inputs or single input is not digit")
# print ("==========================================")
# h=int(input("enete the nput\n"))
# kl=h+50
# print(kl)
#

# #Try and catch block using
# try:
#     a=int(input("Enter the input1\n"))
#     print ("User entered correct input\n and try blck is sucess")
# except:
#     print ("Try block is failed")
#     no_attem=int(input("entere the number of attempts"))
#     for i in range(1,no_attem,1):
#         print ("Attempt number is {0}".format(i))
#         try:
#             a = int(input("Enter the input1\n"))
#             print ("Attemp number {0} is sucess".format(i))
#             break
#         except:
#             print ("Attempt number {0} is failed".format(i))
#             rem=no_attem-i
#             print ("Remainining attemps are {0}".format(rem))


#return method using the code
'''
def p1(a,b):
    c=a+b
    d=a-b
    e=a*b
    print ("Sum of {0} and {1} is {2}\ndifference of {0} and {1} is {3}\nproduct of {0} and {1} is {4}".format(a,b,c,d,e))
    print (c,d,e)
    return c,d
    print (c,d,e)
    print ("Name is vinith")
    print ("=============================")

n1=int(input("Enter the input1\n"))
n2=int(input("Enterthe input2\n"))
satish=p1(n1,n2)
print ("Returned outpit is {0}".format(satish))


#Local And global variable
# Inside the fucntion = local variable
# outside of the function = global variable


def p1():
    global a
    a=100
    print ("Value is {0} after assigning new value inside function".format(a))

a=int(input("Enter the input\n"))
print ("Value is {0} before calling function".format(a))
p1()
print("Value is {0} after calling function".format(a))

'''

# How to create a file and read of the file in python
# read write and append
