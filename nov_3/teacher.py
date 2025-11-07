# Класс учителей
class Teacher:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def input_grades(self):
        print(f"id преподавателя: {self.id}")
        grades_input = input("Введите оценки (имя:оценка, имя:оценка):")

        grades = {}
        pairs = grades_input.split(',')
        for pair in pairs:
            pair = pair.strip()
            if ':' in pair:
                student, grade = pair.split(':')
                grades[student.strip()] = int(grade.strip())
        
        return grades