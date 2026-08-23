def p1():
    print("Entered input is {0}".format(a))
    print("True")


def p2():
    print("Entered input is {0}".format(a))
    print("False")


a = input("Enter the input\n")

if a == "praveen":
    p1()
elif a == "san":
    p1()
elif a == "abhi":
    p2()
elif a == "ajay":
    p2()
else:
    p1()
    p2()