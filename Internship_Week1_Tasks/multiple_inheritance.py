class Ankit:
    Back = "Oracle DB & Java"
    def Backend(self):
        print("Backend Task implemented using: ", self.Back)

class Ayush:
    Front = "HTML CSS JavaScript"
    def Frontend(self):
        print("Frontend Task implemented using: ", self.Front)

class TeamLead(Ankit, Ayush):
    def Show(self):
        print("Dynamic Website Created....")

T = TeamLead()
T.Backend()
T.Frontend()
T.Show()
    