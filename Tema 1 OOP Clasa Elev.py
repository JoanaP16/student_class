class Student:
    student_catalog = {}

    def __init__ (self, name, surname):
        self.name = name
        self.surname = surname
        self.catalog = []

    def get_marks (self, mark):
        self.mark = mark
        self.catalog.append(mark)
        Student.student_catalog[self.name] = self.catalog

    def student_average(self):
        student_average = float(sum(self.catalog)) / len(self.catalog)

    def overall_average(self):
        sumac = 0  # suma tuturor notelor
        count = 0
        for i in Student.student_catalog:
            for valoare in Student.student_catalog[i]:
                sumac += valoare
                count += 1
        general_average = sumac / count

    def print_detailes(self):
        print(f'Student {self.name}-{self.surname} get average {student_average}. General average is {general_average}')

        with open('student_average.txt', 'a') as file:
            file.write(f' Student {self.name}-{self.surname} has average {self.student_average}',)


Popescu_Melania = Student('Popescu', 'Melania')
Popescu_Melania.get_marks(100)
Manole_Denisa = Student('Manole', 'Denisa')
Manole_Denisa.get_marks(100)
Popescu_Melania.get_marks(90)
Manole_Denisa.get_marks(75)
Manole_Denisa.student_average()
