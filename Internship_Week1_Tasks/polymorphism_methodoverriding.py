class A: #Parent
    def Disp(self):
        print("This is parent class method")

class B(A): #Child
    def Disp(self):
        super().Disp() # Used to call parent class function
        print("This is child class method")

obj = B()
obj.Disp()