import csv

class NameValidator:
    def __set__(self, instance, value):
        if not value.isalpha() or not value.istitle():
            raise ValueError("Name must contain only alphabetic characters and start with a capital letter")
        self.value = value

class Subject:
    def __init__(self, name):
        self.name = name
        self.grades = []
        self.scores = []

    def add_grade(self, grade):
        if 2 <= grade <= 5:
            self.grades.append(grade)
        else:
            raise ValueError("Grade must be between 2 and 5")

    def add_score(self, score):
        if 0 <= score <= 100:
            self.scores.append(score)
        else:
            raise ValueError("Score must be between 0 and 100")

    def avg_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def avg_score(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0

class Student:
    name = NameValidator()

    def __init__(self, fio, subjects_file):
        self.fio = fio
        self.subjects = self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file):
        subjects = []
        with open(subjects_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                subjects.append(Subject(row[0]))
        return subjects

    def add_grade(self, subject_name, grade):
        subject = self.find_subject(subject_name)
        subject.add_grade(grade)

    def add_score(self, subject_name, score):
        subject = self.find_subject(subject_name)
        subject.add_score(score)

    def find_subject(self, subject_name):
        for subject in self.subjects:
            if subject.name == subject_name:
                return subject
        raise ValueError("Subject not found")

    def avg_grade_by_subject(self, subject_name):
        subject = self.find_subject(subject_name)
        return subject.avg_grade()

    def avg_score_by_subject(self, subject_name):
        subject = self.find_subject(subject_name)
        return subject.avg_score()

    def overall_avg_grade(self):
        total_grades = sum(subject.avg_grade() for subject in self.subjects)
        return total_grades / len(self.subjects) if self.subjects else 0

    def overall_avg_score(self):
        total_scores = sum(subject.avg_score() for subject in self.subjects)
        return total_scores / len(self.subjects) if self.subjects else 0


student = Student("John Doe", "subjects.csv")

student.add_grade("Math", 5)
student.add_grade("Math", 4)
student.add_score("Math", 90)

student.add_grade("Physics", 3)
student.add_score("Physics", 80)

print(f"Average grade in Math: {student.avg_grade_by_subject('Math')}")
print(f"Average score in Math: {student.avg_score_by_subject('Math')}")

print(f"Average grade in Physics: {student.avg_grade_by_subject('Physics')}")
print(f"Average score in Physics: {student.avg_score_by_subject('Physics')}")

print(f"Overall average grade: {student.overall_avg_grade()}")
print(f"Overall average score: {student.overall_avg_score()}")
