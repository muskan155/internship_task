class Father:
    def __init__(self, f_name):
       self.f_name = f_name
class Mother:
    def __init__(self, m_name):
       self.m_name = m_name
    def my_mum_name(self):
        print(f"My mother name is {self.m_name}")
class Child(Father, Mother):
    def __init__(self, c_name, f_name, m_name):
       self.c_name = c_name
       Father.__init__(self, f_name)
       Mother.__init__(self, m_name)

c1 = Child(c_name = "Lov-Kush", f_name = "Ram", m_name = "Sita")
c1.my_mum_name()