# a=input("Enter the input\n")
# if (a.isalpha()):
#     print ("{0} is alpha".format(a))
#     if (a.isupper()):
#         print ("{0} is in uppercase".format(a))
#         opt=input("Enter '1' to conbery to lowercase\n")
#         if (opt == "1"):
#             print ("User confirmed to convert to lowercase\n")
#             conv_a=a.lower()
#             if (conv_a.islower()):
#                 print ("Orginal string conveted to lower orgial string is {0} convered is {1}".format(a,conv_a))
#             else:
#                 print ("Orginal string not converted to lower post user coformation"
#                 else:
#                 print ("User not confrmed to convert to lower case\n")
#                 elif (a.islower()):
#                 print ("{0} is in lowercase".format(a))
#                 elif (not a.isupper() and not a.islower()):
#                 print ("{0} is not upper or lower".format(a))
#                 else:
#                 print ("{0} is not alphabet".format(a))
#
#
#
#                 -------------------------------------------------------
# 20.06.206 class (all program like lowe to upper and and print in the output , using user input value) in one script
# a=input("Enterthe user input\n")
# if (a.isalpha()):
#     print ("{0} is alphabet".format(a))
#     opt=int(input("Enter '1' to convert to lowrrcase\n'2'  convert to upper\n'3' to swap"))
#     if (opt == 1):
#         if (a.islower()):
#             print ("{0} is already in lower case".format(a))
#         else:
#             conv=a.lower()
#             print ("Orginal string is {0} and conveed to lower is {1}".format(a,conv))
#
#     elif (opt == 2):
#         if (a.isupper()):
#             print ("{0} is in uppercase".format(a))
#         else:
#             conv=a.upper()
#             print ("Orginal string {0}  and conveted to uppr is {1}".format(a,conv))
#     elif (opt == 3):
#         print ("orginal is {0} and swapped case is {1}".format(a,a.swapcase()))
#
# elif (a.isdigit()):
#     print ("{0} is digit".format(a))
#     kl=int(input("Enter another number\n"))
#     if (int(a)%2 == 0):
#         print ("{0} is even".format(a))
#         opt=int(input("ENter'1' to add\n'2' to sub\n"))
#         if (opt == 1):
#             adds=int(a)+kl
#             print ("sum of {0} and {1} is {2}".format(a,kl,adds))
#         elif (opt == 2):
#             ss=int(a)-kl
#             print ("Difference of {0} and {1} is {2}".format(a,kl,ss))
#
#     elif (int(a)%2 != 0):
#         print ("{0} is odd".format(a))
#         opt=int(input("ENter '1' to mul\n'2' to divi\n"))
#         if (opt == 1):
#             mus=int(a)*kl
#             print ("Product of {0} and {1} is {2}".format(a,kl,mus))
#         elif (opt == 2):
#             dis=int(a)/kl
#             print ("quotient of {0} an {1} is {2}".format(a,kl,dis))
# elif (not a.isdigit() and not a.isalpha()):
#     print ("{0} is not digit and not alpha".format(a))



#->Whether input is present in the list using if else condition
alist=['praveen','hemanth','san','10','20','san1234']
inp=input("ENte the input to be checked\n")
if (inp in alist):
    print ("{0} is present in list".format(inp))
    if (inp.isalpha()):
        print ("{0} is alphabet".format(inp))
        lk=input("Ente the another input\n")
        nj=inp+lk
        alist.append(nj)
        print (alist)
    elif (inp.isdigit()):
        print ("{0} is digit".format(inp))
else:
    print ("{0} not present in list".format(inp))
    opt=input("ENter 'yes' to add item to list\n")
    if (opt  == "yes"):
        print ("User confirmed to add to list\n")
        alist.append(inp)
        if (inp in alist):
            print ("{0} successfully added to list post user confirmation".format(inp))
            print (alist)







