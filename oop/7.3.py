# 3. Create a Student class that stores name and grades, and can compute the average.

class Student:
    """
    A class to represent a student with a name and list of grades.
    """

    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        """
        Adds a grade to the student's record.
        """
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("Invalid grade. Must be between 0 and 100.")

    def average(self):
        """
        Returns the average of the student's grades.
        """
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

student = Student("Saket")
student.add_grade(85)
student.add_grade(90)
student.add_grade(78)

print(f"Average grade for {student.name}: {student.average():.2f}")