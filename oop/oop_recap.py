class Universal:
    uniqieId = 0
    def __init__(self,name,id,dept) -> None:
        self.name = name
        self.id = id
        self.dept = dept
        Universal.uniqieId += 1


    def printInfo(self):
        print("Name:",self.name)
        print("Id:",self.id)
        print("Department:",self.dept)

    def __add__(self,other):
        return self.name+other.name
    def __str__(self) -> str:
        return f"{self.id}"



class Student(Universal):
    def __init__(self,name,id,dept,passion,semester) -> None:
        super().__init__(name,id,dept)
        self.semester = semester
        self.passion = passion
        self.__uniqueId = Universal.uniqieId



    def printInfo(self):
        super().printInfo()
        print("Passion: ",self.passion)
        print("Semester:",self.semester)

    def getUniqueId(self):
        print("Unique ID: ",self.__uniqueId)





class Teacher(Universal):
    def __init__(self, name, id, dept,passion,cy) -> None:
        super().__init__(name, id, dept)
        self.contractYear = cy
        self.passion = passion
        self.__uniqueId = self.uniqieId


    def printInfo(self):
        super().printInfo()
        print("Passion: ",self.passion)
        print("Contract Year: ",self.contractYear)


    def getUniqueId(self):
        print("Unique ID: ",self.__uniqueId)
    
    

std1 = Student("Naimur",22101075,"CSE","Student","5th")
std1.printInfo()
std1.getUniqueId()
print("#"*20)
std2 = Student("Naimur",22101075,"CSE","Student","5th")
std2.getUniqueId()

print("#"*20)

teacher1 = Teacher("TMD","#321","CSE","Teacher",2)
teacher1.printInfo()
teacher1.getUniqueId()