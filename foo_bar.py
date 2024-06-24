num = int(input("Enter a number: "))
if num % 7 == 0 and num % 5 == 0:
       print("foobar")
elif num % 7 == 0:
       print("foo")
elif num % 5 == 0:
       print("bar")
else:
       print(num)