# Write a program which says that if a number is divisible by 7 print foe, if the number is divisible by 5 print bar and if it is divisible by both 7 and 5 then print foebar.

num =int(input("Enter a number: "))
if num % 7 == 0 and num % 5 == 0:
    print("FoeBar")
elif num % 7 == 0:
    print("Foe")
else:
    print("Bar")