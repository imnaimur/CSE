class Student:
    def __init__(self,x,y) -> None:
        self.name = x
        self.id = y
    def addition (self):
        self.sum = 0
        return self.sum
    @classmethod
    def cgpa (cls,name,id):
        return Student(name,id)

test = Student.cgpa("naimur",22101075)
print(test.name)