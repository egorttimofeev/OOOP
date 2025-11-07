# Класс заданий
class Task:
    def __init__(self, id, name, hours, teacher_id, discipline_id, group_id):
        self.id = id
        self.name = name
        self.hours = int(hours)
        self.teacher_id = int(teacher_id)
        self.discipline_id = int(discipline_id)
        self.group_id = int(group_id)