class A:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    def Add(self):
        print("Addition: ", self.num1+self.num2)
    def Sub(self):
        print("Subtraction: ", self.num1-self.num2)


class B(A):
    def Multi(self):
        print("Multiplication: ", self.num1*self.num2)
    def Div(self):
        print("Division: ", self.num1/self.num2)
    def Rem(self):
        print("Remainder: ", self.num1%self.num2)

obj=B()
obj.Add()
obj.Sub()
obj.Multi()
obj.Div()
obj.Rem()