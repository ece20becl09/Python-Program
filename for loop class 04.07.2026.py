#for i in range (st,end,jump):
#    <block>

# 1. This is the basic question:-

# for i in range(0,20,1):
#     print(i)


#2. Increment the value and display in the output what value is increased
# inp=int(input("Enter the input\n"))
# for i in range(0,20,1):
#     co=i+inp
#     print ("Orginal input is {0} incremneted by {1} and output is {2}".format(i,inp,co))


# 3.Write a Python program that iterates from 0 to 19. In each iteration, accept an integer from the user,
# add it to the current
# loop index, and display the original index, the user input, and their sum.

# for i in range(0,20,1):
#     inp = int(input("Enter the input\n"))
#     co = i + inp
#     print("Orginal input is {0} incremneted by {1} and output is {2}".format(i, inp, co))


#4.Write a Python program that:
# Accepts an integer from the user.
# Iterates from 0 to 19 using a for loop.
# For every iteration except 15 and 19, prints the sum of the loop index and the entered number.
# When the loop index is 15 or 19, accepts another integer from the user, subtracts it from the sum, and prints the result.

# inp=int(input("Ente the another number\n"))
# for i in range(0,20,1):
#     if (i == 15) or (i == 19):
#         anp=int(input("Ente the addition input\n"))
#         mkl=i+inp-anp
#         print ("sum of {0} and {1} with differece if {2} is {3}".format(i,inp,anp,mkl))
#     else:
#         hj=i+inp
#         print ("sum of {0} and {1} is {2}".format(i,inp,hj))


#5. Write a Python program to find and display the cumulative (running) sum of numbers from 0 to 19 using a for loop.
# k=0
# for i in range (0,20,1):
#     k=k+i
#     print(k)


#6.Write a Python program that accepts an integer from the user and iterates from 0 to 19. Depending on the value
# of the loop counter, perform different arithmetic operations as follows:

# For values from 1 to 5, print the sum of the loop counter and the input.
# For values from 6 to 10, print the difference of the loop counter and the input.
# For values from 11 to 15, print the product of the loop counter and the input.
# For values from 16 to 19, print the sum, difference, and product.


inp = int(input("Enter the Value By User input\n"))
for i in range(0, 20, 1):
    if (i > 0) and (i < 6):
        adds = i + inp
        print("Sum of {0} and {1} is {2}".format(i, inp, adds))
    elif (i > 5) and (i < 10):
        sus = i - inp
        print("Difference of {0} and {1} is {2}".format(i, inp, sus))
    elif (i > 10) and (i < 16):
        mus = i * inp
        print("product of {0} and {1} is {2}".format(i, inp, mus))

    elif (i > 15) and (i < 20):
        adds = i + inp
        sus = i - inp
        mus = i * inp
        print("Sum of {0} and {1} is {2}".format(i, inp, adds))
        print("Difference of {0} and {1} is {2}".format(i, inp, sus))
        print("product of {0} and {1} is {2}".format(i, inp, mus))
    print("===================================================")
