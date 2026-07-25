# # #1. Print Numbers(1-20)
# # for i in range(1, 100):
# #     print(i)
#
# # #2. Even Or Odd Number To Show
# # n = int(input("Enter a number: "))
# #
# # for i in range(1, n + 1):
# #     if i % 2 == 0:
# #         print(i, "is even")
# #     else:
# #         print(i, "is odd")
#
# # #3. Multplication Table
# # num = int(input("Enter a number: "))
# # for i in range(1, 11):
# #     print(f"{num}* {i}={num * i}")
#
# # #4. Sum Of Even Numbers
# # total =0
# # for i in range(1, 101):
# #     if i % 2 == 0:
# #         total += i
# #         print("Sum of {0} is {1}".format(i, total))
# #
#
# # #5. Count Digits
# # num= int(input("Enter a number: "))
# # count = 0
# # while num > 0:
# #     num = num // 10
# #     count += 1
# #     print("Digits =", count)
#
#
# # #6. Revers Pattern
# # for i in range(5, 0, -1):
# #     for j in range(1, i + 1):
# #         print(i, end=" ")
# #         print()
#
# #7Fizz Buzz
# # for i in range(1, 51):
# #     if i % 3 ==0 and i % 5 == 0:
# #         print("FizzBuzz")
# #     elif i % 3 == 0:
# #         print("Fizz")
# #     elif i % 5 == 0:
# #         print("Buzz")
# #     else:
# #         print(i)
#
# #8. Calculator
#
#
# # Get first number
# while True:
#     try:
#         num1 = float(input("Enter first number: "))
#         break
#     except ValueError:
#         print("Invalid input! Please enter a valid number.\n")
#
# # Get second number
# while True:
#     try:
#         num2 = float(input("Enter second number: "))
#         break
#     except ValueError:
#         print("Invalid input! Please enter a valid number.\n")
#
# # Display menu
# print("\nChoose an operation:")
# print("1. Addition (+)")
# print("2. Subtraction (-)")
# print("3. Multiplication (*)")
# print("4. Division (/)")
#
# # Get valid choice
# while True:
#     try:
#         choice = int(input("Enter your choice (1-4): "))
#         if 1 <= choice <= 4:
#             break
#         else:
#             print("Please enter a number between 1 and 4.\n")
#     except ValueError:
#         print("Invalid choice! Please enter a number between 1 and 4.\n")
#
# # Perform calculation
# if choice == 1:
#     print("Answer =", num1 + num2)
#
# elif choice == 2:
#     print("Answer =", num1 - num2)
#
# elif choice == 3:
#     print("Answer =", num1 * num2)
#
# elif choice == 4:
#     if num2 == 0:
#         print("Cannot divide by zero!")
#     else:
#         print("Answer =", num1 / num2)
#
# #7. Range Operations
# for i in range(1, 31):
#
#     if i <= 10:
#         print(i, "Square =", i ** 2)
#
#     elif i <= 20:
#         print(i, "Cube =", i ** 3)
#
#     else:
#         print(i, "Square =", i ** 2, "Cube =", i ** 3)

# a="praveenajaysankumarabhi"
# for i in range(0,len(a),1):
#     if (a[i] == "a") or (a[i] == "e"):
#         print ("{0} present in position {1}".format(i,a[i]))
#


# import winsound
#
# number = 10
# expected = 20
#
# try:
#     assert number == expected, "Logic Mismatch!"
#
#     print("Correct Logic")
#
# except AssertionError as e:
#     winsound.MessageBeep(winsound.MB_ICONHAND)
#     print(e)

import sys
import winsound

number = 10
expected = 20

try:
    assert number == expected, (
        f"Logic mismatch: expected {expected}, but got {number}"
    )

    print("Logic is correct")

except AssertionError as error:
    print(error)
    winsound.Beep(1000, 1000)
    sys.exit(1)