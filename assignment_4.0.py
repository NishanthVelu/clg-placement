#Birth

class Child:

    def __init__(self, name, gender,weight):
        self.name = name
        self.gender = gender
        self.weight = weight

    def birth_details(self):
        print("A child emerges the earth.")
        print("Name:",self.name)
        print("Gender:",self.gender)
        print("Weight:",self.weight, "kg" )

    
child_0 = Child("Ziyan","Male",4.0)
child_0.birth_details()

child_1 = Child("Ziya","Female",3.4)
child_1.birth_details()

child_2 = Child("Ram","Male",4.5)
child_2.birth_details()



class child_to_school:

    def __init__(self,name,age,grade,sex):
        self.name = name
        self.age = age
        self.grade = grade
        self.sex = sex

    def can_appear_for_admission(self,eligibility):
        if self.age >= eligibility["Age_Bar"]:
            return True
        else:
            return False



class School_system:

    def __init__(self):
        self.students = {}
        self.students_joined = {}
        self.students_rejected = {}
        self.students_on_hold = {}

    def add_student(self,student):
        self.students[student.name] = student

    def register_student_for_admission(self,student):
        self.add_student(student)

    def process_admission(self,school_name,eligibility):
        eligible_students = []
        for student_name, student in self.students.items():
            if eligible_students.can_appear_for_admission(eligibility):
                eligible_students.append(student_name)

        print(f"Eligible students for {school_name}: {','.join(eligible_students)}")

        if eligible_students:
            self.student_joined.append(eligible_students[0])
            print(f"{eligible_students[0]} is got adimitted at {school_name}.")

        
student_1 = child_to_school("Ziyan",6,"Grade 1","Male")
student_2 = child_to_school("Ziya",5,"Grade 1","Female")
student_3 = child_to_school("Ram",7,"Grade 1","Male")

adimission_system = School_system()

adimission_system.register_student_for_admission(student_1)
adimission_system.register_student_for_admission(student_2)
adimission_system.register_student_for_admission(student_3)

eligibility_age = {"Age_Bar": 6} 

adimission_system.process_admission("Freedom Concept School", eligibility_age)