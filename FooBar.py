num = int(input("Enter a number: "))
if num % 7 == 0 and num % 5 == 0:
    print("FooBar")
elif num % 7 == 0:
    print("Foo")
elif num % 5 == 0:
    print("Bar")
else:
    print("num")