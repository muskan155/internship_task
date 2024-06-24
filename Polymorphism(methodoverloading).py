class A:
    def Show(self):
        print("Welcome")

    def Show(self, firstname=''):
        print("Welcome", firstname)

    def Show(self, firstname='', lastname=''):
        print("Welcome", firstname, lastname)

obj = A()
obj.Show()
obj.Show('Muskan')
obj.Show("Muskan", "Rauniyar")