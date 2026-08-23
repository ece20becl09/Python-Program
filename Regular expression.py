# #import re (regular expression)
#
# import re
# k="praveeenajaysankiran"
# pa=re.compile(r'a')
# try:
#     kp=re.search(pa,k)
#     print (kp)
#     print (kp.group())
#     print ("Pattern found is {0} in {1}".format(kp.group(),k))
# except Exception as e:
#     print ("Pattern not found and error is {0}".format(e))
#

#| using or symbol
# import re
# mainstr = "praveen ajay san kiran surya"
# pa = re.compile(r'ashim|kiran1234')
# try:
#     kp = re.search(pa, mainstr)
#     fou_item = kp.group()
#     print(fou_item)
# except Exception as e:
#     print("pattern not found")
#

#through user input value:-
#
# import re
# mainstr="praveen ajay san kiran surya"
# inp1=input("Enter the pattern1\n")
# inp2=input("Enter the pattern2\n")
# pa=re.compile(r'{0}|{1}'.format(inp1,inp2))
# try:
#     kp=re.search(pa,mainstr)
#     fou_item=kp.group()
#     print ("Any one or both items matched and matched is {0}".format(fou_item))
#     if (inp1 == fou_item ):
#         print ("First input is matched and matces string is {0}".format(fou_item))
#     elif (inp2 == fou_item):
#         print ("Second input is matched and matched string is {0}".format(fou_item))
# except Exception as e:
#     print ("pattern not found")


#throguh and condition using the re expression:-
mainstr="praveen ajay san kiran surya"
import re
inp1=input("Enter the input1\n")
inp2=input("Enter the input2\n")
pa1=re.compile(r'{0}'.format(inp1))
pa2=re.compile(r'{0}'.format(inp2))
#kp = re.search(pa1,mainstr) and re.search(pa2,mainstr)
#print (kp.group())
try:
    kp=re.search(pa1,mainstr) and re.search(pa2,mainstr)
    print (kp.group())
    print ("Both inpus are present  final captured elemeht is {0}".format(kp.group()))
except:
    print ("Patrern not found")