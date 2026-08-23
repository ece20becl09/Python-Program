# Program to Compare Two Lists for Equality
# import comm
# NO IMPORTS NEEDED! Global error handler auto-activated!

# alist=['praveen','ajay','san','satish','rajesh','rajesh']
# blist=['san','ajay','praveen','rajesh']
# common_items=[]
# if (len(alist) == len(blist)):
#     print ("There is channce both lists can be same")
#     for i in range(0,len(alist),1):
#         if (alist[i] in blist):
#             common_items.append(alist[i])
#     print (common_items)
#     if (len(common_items) == len(alist)) and (len(alist) == len(blist)) and (len(blist) == len(common_items)):
#         print ("Both lists are same")
#     else:
#         print ("Both lists are not same")
#
# else:
#     print ("Both lists are not same")

# Program to Find and Store Common Elements Between Two Lists
# alist=['abhi','praveen','shashank','nitin','shivu','darshan']
# blist=['praveen','ajay','san','satish']
#
# commonelement=[]
# fist_not_in_second=[]
# for i in alist:
#     if (i in blist):
#         commonelement.append(i)
#     elif (i not in blist):
#         fist_not_in_second.append(i)
# print ("Common elements are {0}".format(commonelement))
# print ("First list ement not in second list is {0}".format(fist_not_in_second))

# Program to Compare Two Lists Element by Element

# alist=['praveen','ajay','san','subham bharama']
# blist=['praveena','ajay','shivani','subham bharama']
# common=[]
# if (len(alist) == len(blist)):
#     print ("Both lists length are same so both may be or may not be same")
#     for i in range(0,len(alist),1):
#         if (alist[i] == blist[i]):
#             common.append(alist[i])
#     if (alist == blist == common):
#         print ("Both lists are same")
#     else:
#         print ("Both lists are not same")
# else:
#     print ("Both lists are not same")

# Program to Traverse and Display Dictionary Elements ✅
# dictionaries = {
#     'a': '10',
#     'b': '20',
#     'c': '30',
#     'd': '40',
#     'e': '50',
#     'f': '60'
# }
#
# for key, value in dictionaries.items():
#     print(key, value)

# Program to Find Key When Value is "praveen"
# dictdetails={'a':'10','b':'20','c':'30','d':'praveen','e':'ajay'}
# for i in dictdetails:
#     if (dictdetails[i] == "praveen"):
#         print (i,dictdetails[i])


# dictdetails={'a':'10','b':'20','c':'30','d':'praveen','e':'ajay'}
# listdetails=['praveen','ajay','san']
# inp=input("ENter the strng to be checked\n")
# for i in dictdetails:
#     if (dictdetails[i] == inp):
#         print (i,dictdetails[i])
#         if (inp in listdetails):
#             print ("{0} prese in list and dict".format(inp))
#             listdetails.remove(inp)
# print (listdetails)

# LOGIC ERROR EXAMPLE CODE
# This code has a logic error that will cause an exception

print("Finding largest number in list...")

numbers = [5, 10, 3, 8, 15]

# LOGIC ERROR: Wrong condition - will try to access index that doesn't exist
largest = numbers[0]
for i in range(1, len(numbers) + 1):  # ERROR: range should be len(numbers), not len(numbers) + 1
    if numbers[i] > largest:
        largest = numbers[i]

print(f"Largest number: {largest}")




