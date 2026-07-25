# #Dictionary Today Class
# #There is two list is there which one is common element , which element is there one element and also not present in the second element
# alist=['praveen','hemanth','san','10','20','san1234']
# blist=['ajay','san','abhi']
# inp=input("Enter the input\n")
# if (inp in alist) and (inp in blist):
#     print ("{0} present in both list".format(inp))
#     pos_list1=alist.index(inp)
#     pos_list2=blist.index(inp)
#     print ("{0} present in postion {1} in list1\n {0} present in positio {2} in list2".format(inp,pos_list1,pos_list2))
# elif (inp in alist) and (inp not in blist):
#     print ("{0} in list1 not in list2".format(inp))
#     post_list21=alist.index(inp)
#     if (post_list21%2 == 0):
#         print ("{0} present in even position {1}".format(inp,post_list21))
#         alist.remove(inp)
#         print (alist)
#     elif (post_list21%2 != 0):
#         print("{0} present in odd position {1}".format(inp, post_list21))
#         anp=input("Eter the another input\n")
#         lp=inp+anp
#         alist[post_list21]=lp
#         print (alist)
# elif (inp not in alist) and (inp in blist):
#     print ("{0} in list2 not in list1".format(inp))
# elif (inp not in alist) and (inp not in blist):
#     print ("{0} not in list1 and list2".format(inp))
#     alist.append(inp)
#     blist.append(inp)
#     print (alist)
#     print (blist)
#
#->If length of list greater then list2 particular string is present in the lsit or not

# alist=['praveen','hemanth','san','10','20','san1234']
# blist=['ajay','san','abhi']
# len_a=len(alist)
# len_b=len(blist)
# if (len_a>len_b):
#     print ("legth of list1 is {0} ad its greater tha list2 length {1}".format(len_a,len_b))
#     inp=input("EnTER THE INPT TO BE CHECKED\n")
#     if (inp in alist):
#         print ("{0} in list1".format(inp))
#         post=alist.index(inp)
#         print("{0} in list1 and its position {1}".format(inp,post))
#     else:
#         print ("{0} not in list1".format(inp))
#         opt=input("ENer yes to insert\n")
#         post_ins=int(input("Enter the posutio\n"))
#         alist.insert(post_ins,inp)
#         print (alist)
#
# elif (len_a == len_b):
#     print ("Both list leghth is same is {0}".format(len_a))
# elif (len_a <len_b):
#     print ("legth of list1 is {0} and is lessser than list2 is length {1}".format(len_a,len_b))
#     items_missin=len_b-len_a
#     print ("ount of items missing {0} in list1".format(items_missin))


#USING KEY VALUE FETCHING:-
bdict={'ajay':'10','san':'20','sriram':'30'}
inp=input("Enter te input\n")
if (inp  in bdict):
    print ("{0} present in dcti".format(inp))
    print (bdict[inp])
elif (inp not in bdict):
    print ("{0} not present in dict".format(inp))
    newva=input("enete the vaue\n")
    bdict[inp]=newva
    print (bdict)