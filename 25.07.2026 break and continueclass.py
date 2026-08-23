# a="praveen"
# for i in a:
#     if (i == "a"):
#         break
#     else:
#         print (i)
from jinja2.ext import loopcontrols

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
# alist=['praveen','san','san','kiran','san','ashimz','sumit','san','ashok','san']
# for i in alist:
#     if('z' in i):
#         break
#     else:
#         print (i)

# Divide each number by 2, if odd print, if even break

# alist=['10','23','34','44','55','66','78']
# for i in alist:
#     if (int(i)%2 == 0):
#         print ("Number {0} is even".format(i))
#         anp=int(input("Enter the another input\n"))
#         opt=int(input("entere '1' to add\n'2' to sub"))
#         if (opt == 1):
#             sop=int(i)+anp
#             if (sop%2 == 0):
#                 break
#             else:
#                 print ("Sum is {0}".format(sop))
#         elif(opt == 2):
#             mop=int(i)-anp
#             print ("Differenn is {0}".format(mop))
#     else:
#         print ("Number {0} is odd".format(i))
#     print ("===================================================")


# 26.07.2026 class break and continue class
#continue :- when ever condition mathces it will ingonre the condition and continure the loopcontrols

# a="praveen"
# for i in a:
#     if (i  == "a"):
#         continue
#     else:
#         print (i)

# #Traverses every character in the string.
#
# a="praveenbesantpythonajayeagle"
# for i in range(0,len(a),1):
#     if (i%2 != 0):
#         if (a[i] == "e"):
#             continue
#         else:
#             print (a[i],i)
#     else:
#         print (a[i],i)

# Break the Loop at the First Index Divisible by Both 3 and 5

# a="praveenbesantpythonajayeagle"
# for i in range(0,len(a),1):
#     if (i%3 == 0) and (i%5 == 0):
#         break
#     else:
#         print (a[i],i)


# for i in range(1,20,1):
#     if(i%2==0):
#         continue
#     else:
#         print(i)


blistco=[22,34,44,55,64,84,95,43,45]

for i in range(0,len(blistco),1):
    if (i%2 == 0):
        if (blistco[i]%2 != 0):
            continue
        else:
            print (blistco[i],i)
    else:
        print (blistco[i],i)