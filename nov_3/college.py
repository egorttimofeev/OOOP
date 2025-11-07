'''
Задания 11
2.	Спроектировать классы: Преподаватель, Группа, Дисциплина, Занятие, Журнал занятий. Построить диаграмму классов.
3.	Написать программу, демонстрирующую работу с классами. Сформировать и вывести в Excel отчет преподавателя о выполнении нагрузки. Данные хранить в текстовых файлах.
'''
import pandas
from discipline import Discipline
from group import Group
from task import Task
from task_journal import TaskJournal
from teacher import Teacher

# Главный класс с формированием excel отчета о выполнении нагрузки
class College:
    def __init__(self):
        # Загрузка данных
        self.teachers = self.load_teachers('teachers.txt')
        self.groups = self.load_groups('groups.txt')
        self.disciplines = self.load_disciplines('disciplines.txt')
        self.tasks = self.load_tasks('tasks.txt')

        # Создание словарей
        self.teachers_dict = {t.id: t for t in self.teachers}
        self.groups_dict = {g.id: g for g in self.groups}
        self.disciplines_dict = {d.id: d for d in self.disciplines}
    
    # Чтение данных из файлов
    def load_teachers(self, filename):
        teachers = []
        with open(filename, 'r') as f:
            for line in f:
                id, name = line.strip().split(',')
                teachers.append(Teacher(int(id), name))
        return teachers

    def load_groups(self, filename):
        groups = []
        with open(filename, 'r') as f:
            for line in f:
                id, name = line.strip().split(',')
                groups.append(Group(int(id), name))
        return groups

    def load_disciplines(self, filename):
        disciplines = []
        with open(filename, 'r') as f:
            for line in f:
                id, name = line.strip().split(',')
                disciplines.append(Discipline(int(id), name))
        return disciplines

    def load_tasks(self, filename):
        tasks = []
        with open(filename, 'r') as f:
            for line in f:
                id, name, hours, teacher_id, discipline_id, group_id = line.strip().split(',')
                tasks.append(Task(int(id), name, int(hours), int(teacher_id), int(discipline_id), int(group_id)))
        return tasks
    
    # Выбор преподавателя
    def create_report(self):
        print("Доступные преподаватели:")
        for teacher in self.teachers:
            print(f"{teacher.id}: {teacher.name}")
        
        teacher_id = int(input("\nВведите ID преподавателя: "))
        selected_teacher = self.teachers_dict.get(teacher_id)

        # Получение заданий преподавателя
        teacher_tasks = [t for t in self.tasks if t.teacher_id == teacher_id]

        # Ввод оценок для каждого задания
        journals = []
        for task in teacher_tasks:
            print(f"Задание: {task.name}")
            print(f"Группа: {self.groups_dict[task.group_id].name}")
            print(f"Дисциплина: {self.disciplines_dict[task.discipline_id].name}")
            
            grades = selected_teacher.input_grades()
            journals.append(TaskJournal(task.id, grades))

        # Заполнение xlsx файла и его создание
        report = []
        for journal in journals:
            task = [t for t in self.tasks if t.id == journal.task_id][0]
            teacher = self.teachers_dict[task.teacher_id]
            group = self.groups_dict[task.group_id]
            discipline = self.disciplines_dict[task.discipline_id]

            report.append({
                "Преподаватель": teacher.name,
                "Группа": group.name,
                "Дисциплина": discipline.name,
                "Задание": task.name,
                "Часы": task.hours,
                "Оценки": str(journal.grades)
            })

        df = pandas.DataFrame(report)
        df.to_excel("report.xlsx")

college = College()
college.create_report()