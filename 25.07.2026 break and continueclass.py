# a="praveen"
# for i in a:
#     if (i == "a"):
#         break
#     else:
#         print (i)

#if an number found in the odd position then break else print

# a="praveen"
# for i in range(0,len(a),1):
#     if (i%2 != 0):
#         if (a[i] == "e"):
#             break
#     else:
#         print (a[i])


#Break the Loop on the First Positive Even Number

# for i in range(0,20,1):
#     if (i%2 == 0) and (i >0):
#         break
#     else:
#         print (i)

# Print Odd Numbers Until the First Even Multiple of 5
#
# for i in range(2,20,1):
#     if (i%2 == 0):
#         if (i%5 == 0):
#             break
#     else:
#         print (i)

#Stop Loop Execution When a Specific List Element is Found

# alist=['praveen','ajay','san','kiran','sunil']
# for i in alist:
#     if (i == "san"):
#         break
#     else:
#         print (i)

#Print List Elements Until "san" Is Found at Index 7 Using break

# alist=['praveen','san','san','kiran','san','ashim','sumit','san','ashok','san']
# for i in range(0,len(alist),1):
#     if (i%2 != 0):
#         if (i == 7):
#             if (alist[i] == "san"):
#                 break
#         else:
#             print (alist[i])
#     else:
#         print (alist[i])


#Print List Elements Until an Element Contains 'z' Using break
alist=['praveen','san','san','kiran','san','ashimz','sumit','san','ashok','san']
for i in alist:
    if('z' in i):
        break
    else:
        print (i)