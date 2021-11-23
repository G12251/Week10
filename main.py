from Person import Person
class Student (Person):
    def _init_(self,f_name, l-name, id, marks):
    self.id = id
    self.marks = marks
    super(). _init_(f_name, l_name)

    def calculate_average(self):
        total = 0
        for key in self.marks:
            total = total + self.marks[key]
        average = total / len(self.marks)
        return average

    def display_average (self):
        print (self.calculate_average())
