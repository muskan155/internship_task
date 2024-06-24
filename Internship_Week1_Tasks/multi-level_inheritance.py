class Father:
    surname = "Singh"

class Son(Father):
    def Show(self):
        print("Ankit", self.surname)

class GrandSon(Son):
    def Disp(self):
        print("Ayush", self.surname)

s = Son()
s.Show()

GS = GrandSon()
GS.Disp()
GS.Show()



