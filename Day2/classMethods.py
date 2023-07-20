class Students():

    def __init__(self) -> None:
        self.Name = 'Ravi'
        self.Grades = (90,80,90,79)

    def average(self):
        return sum(self.Grades) / len(self.Grades)
    
    # def __str__(self) -> str:
    #     return f'Person is {self.Name} with grades {self.Grades}.'
    
    def __repr__(self) -> str:
        return f'<This is same as str its just its being used by the programmers and called explicitly.>'
    

student = Students()
# print(student.average())
print(student)