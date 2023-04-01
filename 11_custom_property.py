class Student:
    allowd_marks = [1, 2, 3, 4, 5]

    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__marks = []
    
    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"
    
    @property
    def avarage(self):
        return sum(self.__marks) / len(self.__marks)
    
    def set_mark(self, new_mark):
        assert new_mark in self.allowd_marks, f"This value {new_mark} is invalid."
        self.__marks.append(new_mark)

    def report(self):
        print("-"*50)
        print(f"Student name: {self.full_name}")
        print(f"Marks: {self.__marks}")
        print(f"Avarage: {self.avarage}")
        print("-"*50)

    def __str__(self) -> str:
        return self.__last_name


csaba = Student("Kiss", "Csaba")
csaba.set_mark(3)
csaba.set_mark(5)
csaba.set_mark(2)
csaba.set_mark(1)
csaba.set_mark(4)

print(csaba.avarage)