class Student:
    def __init__(self, name="Student", age="Student", class_="Student"):
        self.name = name
        self.age = age
        self.class_ = class_

    def avgscore(self, score1, score2, score3):
        avg = (score1 + score2 + score3)/3
        return f"{self.name} your average score is {avg}"
    
Student1 = Student("Anna", 22, "Math")
Boris = Student("Boris", 21, "Math")
David = Student("David", 22, "Math")
Emma = Student("Emma", 21, "Math")
John = Student ("John", 21, "Math")
Maria = Student("Maria", 22, "Math")
Nash = Student("Nash", 21, "Math")
Student1.avgscore(10, 20, 30)

print(Boris.avgscore(10, 20, 30))


