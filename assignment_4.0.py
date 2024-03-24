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



class grade10:

    def __init__(self,name,free_kid,grade):
        self.name = name
        self.free_kid = free_kid
        self.grade = grade

    def mark(self):
        if self.grade >= 90 and self.grade <= 100:
            return "First Class"
        elif self.grade >= 80 and self.grade <=89:
            return "Second Class"
        elif self.grade >=70 and self.grade <=79:
            return "Third Class"
        else:
            return "Backed, just improve"
        

    def award(self,classaward):
        if classaward("First Class"):
            return "Gold Medal"
        
        elif classaward("Second Class"):
            return "Silver Medal"
        
        else:
            return "Bronze Medal"
        
    

std_1 = grade10("Ziyan",10,91)
std_2 = grade10("Ziya",10,56)
std_3 = grade10("Ram",10,76)

print(f"{std_1.name} got {std_1.mark()} Grade and was awarded with {std_1.award()}.")
print(f"{std_2.name} got {std_2.mark()} Grade and was awarded with {std_2.award()}.")
print(f"{std_3.name} got {std_3.mark()} Grade and was awarded with {std_3.award()}.")



