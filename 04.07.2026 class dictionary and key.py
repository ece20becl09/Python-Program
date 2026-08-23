alist=['ajay','san','kiran']
bdict={'ajay':'10','san':'20','sriram':'30'}

inp=input("Enter the input\n")
if (inp in alist) and (inp not in bdict):
    post=alist.index(inp)
    newitem=input("ENer the new item to be replaced instead of {0}".format(inp))
    alist[post]=newitem
    new_val_dic=input("Enter the value for {0}".format(inp))
    bdict[inp]=new_val_dic
    print (alist)
    print (bdict)
elif (inp not in alist) and (inp not in bdict):

    print ("{0} not in list and not in dict".format(inp))
    conf=input("Enter 'yes' to add to list and dict\n")
    if (conf == "yes"):
        print ("User cnfirmed to add\n")
        alist.append(inp)
        val_list=input("ENter the value for {0}".format(inp))
        bdict[inp]=val_list
        print (alist)
        print (bdict)
    else:
        print ("User not confirmed to add\n")