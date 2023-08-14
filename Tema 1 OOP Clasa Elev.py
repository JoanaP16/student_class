class Student:
    student_catalog = {}

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.catalog = []

    def get_marks(self, mark):
        self.mark = mark
        self.catalog.append(mark)
        Student.student_catalog[self.name] = self.catalog

    def student_average(self):
        return float(sum(self.catalog)) / len(self.catalog)  # daca pun return e mai usor de folosit in afara functiei

    def overall_average(self):
        sumac = 0  # suma tuturor notelor
        count = 0
        for i in Student.student_catalog:
            for valoare in Student.student_catalog[i]:
                sumac += valoare
                count += 1
        return sumac / count

    def print_detailes(self):
        student_avg = self.student_average()
        overall_avg = self.overall_average()
        detailes = f'Student {self.name}-{self.surname} get average {student_avg}. General average is {overall_avg}\n'

        with open('student_average.txt', 'r') as file:
            lines = file.readlines()
            if detailes not in lines:
                print(detailes)
                with open('student_average.txt', 'a') as to_add:
                    to_add.write(detailes)

    @classmethod
    def get_file(cls, file):
        students = []
        with open(file, 'r') as file_class:
            lines = file.readlines()
            for line in lines:
                name, surname = line.strip().split()
                student = cls(name, surname)
                students.append(student)
        return students


Popescu_Melania = Student('Popescu', 'Melania')
Popescu_Melania.get_marks(100)
Manole_Denisa = Student('Manole', 'Denisa')
Manole_Denisa.get_marks(100)
Popescu_Melania.get_marks(90)
Manole_Denisa.get_marks(75)
Manole_Denisa.student_average()
Popescu_Melania.print_detailes()
Manole_Denisa.print_detailes()
Andreescu_Anemona = Student('Andreescu', 'Anemona')

students_get_file = Student.get_file('student_average.txt')
