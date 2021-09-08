
class student():
    def __init__(self, name, year, work_ethic ):
        self.name = name
        self.year = year
        self.work_ethic = work_ethic

    def greeting(self):
        print(f"Hello {self.name}")

    def yearGroup(self):
        if self.year in range(7,10):
            print(f"You are in year {self.year}, thats in lower school") 
        elif self.year in range(10,12):
            print(f"You are in year {self.year}, thats in upper school")
        elif self.year in range(12,14):
            print(f"You are in 6th form")
        else:
            print("you arent in this school")
    
    def working(self):
        if "high" in self.work_ethic:
            print(f"You have a {self.work_ethic} work ethic, well done") 
        elif "med" in self.work_ethic:
            print(f"Your work ethic is only {self.work_ethic}, you need to try a bit harder!")
        elif "low" in self.work_ethic:
            print(f"Your work ethic is {self.work_ethic}, thats really not good enough!")

studentA = student("Katie", 7, "high")
studentB = student("George", 6, "medium")
studentC = student("Hux", 11, "low")

greetstudentA = studentA.greeting() 
schoolYearA = studentA.yearGroup()
ethicA = studentA.working()
 
greetstudentB = studentB.greeting() 
schoolYearB = studentB.yearGroup()
ethicB = studentB.working()

greetstudentC = studentC.greeting() 
schoolYearC = studentC.yearGroup()
ethicC = studentC.working()


