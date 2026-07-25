#Write a Python program to search for an element in a list.
# If the element is found, verify its position. Otherwise,
# ask the user whether to insert the element at a specified position and display the updated list.


# alist=['praveen','ajay','san','kiran','123','10','5','6']
# pos=int(input("Enter the position number\n"))
# inp=input("Enter the input\n")
# if (inp in alist):
#     print ("{0} is present  in list".format(inp))
#     for i in range(0,len(alist),1):
#         if (i == pos) and (alist[i] == inp):
#                 print ("{0} present in particular position {1}".format(inp,i))
#
# else:
#     print ("{0} not present in list".format(inp))
#     opt=input("Enter 'yes' to add\n")
#
#     if (opt == "yes"):
#         post_inser = int(input("enter the position number\n"))
#         print ("user confirmd to add")
#         alist.insert(post_inser,inp)
#         print (alist)
#         if (alist[post_inser] == inp):
#             print ("{0} got successfullt inserted in position {1}".format(inp,post_inser))
#     else:
#         print ("user not confirmed to add")



#Python Program to Search an Element in a List, Verify Its Position, Search a Character in the Element,
#and Insert the Element if Not Found


# alist=['praveen','ajay','san','kiran','123','10','5','6']
#
# pos=int(input("Enter the position number\n"))
# inp=input("Enter the input\n")
# if (inp in alist):
#     print ("{0} is present  in list".format(inp))
#     for i in range(0,len(alist),1):
#         if (i == pos) and (alist[i] == inp):
#                 print ("{0} present in particular position {1}".format(inp,i))
#                 ch_chec=input("Enter the character to be checked\n")
#                 if(ch_chec in alist[i]):
#                     print ("{0} present in {1}".format(ch_chec,alist[i]))
#                     post_cha_ch=int(input("enter the chaacter position\n"))
#                     cpa_char=alist[i].index(ch_chec)
#                     if(cpa_char == post_cha_ch):
#                         print ("{0} preset in position {1} in string {2}".format(ch_chec,post_cha_ch,alist[i]))
#                     else:
#                         print("{0} not preset in position {1} in string {2}".format(ch_chec, post_cha_ch, alist[i]))
#                 else:
#                     print ("{0} not preseny in {1}".format(ch_chec,alist[i]))
#
# else:
#     print ("{0} not present in list".format(inp))
#     opt=input("Enter 'yes' to add\n")
#
#     if (opt == "yes"):
#         post_inser = int(input("enter the position number\n"))
#         print ("user confirmd to add")
#         alist.insert(post_inser,inp)
#         print (alist)
#         if (alist[post_inser] == inp):
#             print ("{0} got successfullt inserted in position {1}".format(inp,post_inser))
#     else:
#         print ("user not confirmed to add")



# Program to Compare List Length with a Threshold and Display Elements Based on Item Length

# alist=['praveen','ajay','san','kiran','123','elephant','10','5','6']
# list_threshold=int(input("Enter the threshod length of list\n"))
# if (len(alist) > list_threshold):
#     print ("length of list is greater than {0} and length of lis is {1}".format(list_threshold,len(alist)))
#     item_threshold=int(input("enter the item threshold\n"))
#     for i in range(0,len(alist),1):
#         if (len(alist[i]) > item_threshold):
#             print (alist[i])
# else:
#     print ("length of listis lesser than {0} and length of list is {1}".format(list_threshold,len(alist)))
#     co_items=list_threshold-len(alist)
#     print ("Count of items missing when compaed to threshold is {0}".format(co_items))

#Program to Validate List Threshold and Dynamically Expand the List

alist=['praveen','ajay','san','kiran','123','elephant','10','5','6']
list_threshold=int(input("Enter the threshod length of list\n"))
if (len(alist) > list_threshold):
    print ("length of list is greater than {0} and length of lis is {1}".format(list_threshold,len(alist)))
    item_threshold=int(input("enter the item threshold\n"))
    for i in range(0,len(alist),1):
        if (len(alist[i]) > item_threshold):
            print (alist[i])
else:
    print ("length of listis lesser than {0} and length of list is {1}".format(list_threshold,len(alist)))
    co_items=list_threshold-len(alist)
    print ("Count of items missing when compaed to threshold is {0}".format(co_items))
    for j in range(0,co_items,1):
        item_add=input("Enter the item to be added\n")
        alist.append(item_add)
    print (alist)
    if (len(alist) == list_threshold):
        print ("items are successfully added")