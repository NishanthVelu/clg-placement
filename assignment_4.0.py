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



class ChildToSchool:

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



class SchoolSystem:

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
            if eligible_students:
                eligible_students.append(student_name)


        print(f"Eligible students for {school_name}: {','.join(eligible_students)}")

        if eligible_students:
            self.student_joined.append(eligible_students[0])
            print(f"{eligible_students[0]} is got adimitted at {school_name}.")

        else:
            print(f"Student is not eligible.")

        
student_1 = ChildToSchool("Ziyan",6,"Grade 1","Male")
student_2 = ChildToSchool("Ziya",5,"Grade 1","Female")
student_3 = ChildToSchool("Ram",7,"Grade 1","Male")

adimission_system = SchoolSystem()

adimission_system.register_student_for_admission(student_1)
adimission_system.register_student_for_admission(student_2)
adimission_system.register_student_for_admission(student_3)

eligibility_age = {"Age_Bar": 6} 

adimission_system.process_admission("Freedom Concept School", eligibility_age)  



class Grade10:

    def __init__(self,name,free_kid,grade,award):
        self.name = name
        self.free_kid = free_kid
        self.grade = grade
        self.award = award

    def mark(self):
        if self.grade >= 90 and self.grade <= 100:
            return "First Class"
        elif self.grade >= 80 and self.grade <=89:
            return "Second Class"
        elif self.grade >=70 and self.grade <=79:
            return "Third Class"
        else:
            return "Backed, just improve"
        

    def ClassAward(self):
        if self.award("First Class"):
            return "Gold Medal"
        
        elif self.award("Second Class"):
            return "Silver Medal"
        
        else:
            return "Bronze Medal"
        
    

std_1 = Grade10("Ziyan",10,91)
std_2 = Grade10("Ziya",10,56)
std_3 = Grade10("Ram",10,76)

print(f"{std_1.name} got {std_1.mark()} Grade and was awarded with {std_1.award()}.")
print(f"{std_2.name} got {std_2.mark()} Grade and was awarded with {std_2.award()}.")
print(f"{std_3.name} got {std_3.mark()} Grade and was awarded with {std_3.award()}.")




class College:

    def __init__(self,name):
        self.name = name
        self.degree = None

    def choose_degree(self,degree):
        self.degree = degree

degree_to_choose = ["engineering","medicine","defence"]

import random

for student in College:
    degree_choice = random.choice(degree_to_choose)
    student.choose_degree(degree_choice)
    degree_to_choose.remove(degree_choice)

student1 = College("Ziyan")
student2 = College("Ziya")
student3 = College("Ram")

for student in College:
    print(f"{student1.name} chooses to study {student1.degree}.")
    print(f"{student2.name} chooses to study {student2.degree}.")
    print(f"{student3.name} chooses to study {student3.degree}.")



class Placement:
    def __init__(self,name,cgpa,hhlc_score,attendence):
        self.name = name
        self.cgpa = cgpa
        self.hhlc_score = hhlc_score
        self.attendence = attendence

    def can_appear_for_interview(self,company_criteria):
        if self.cgpa >= company_criteria["cgpa_criteria"] and self.attendence >= company_criteria["attendence_criteria"]:
            return True
        else:
            return False
        
    class Placementsystem:
        def __init__(self):
            self.students = {}
            self.placed_students = []
            self.rejected_students = []
            self.students_on_hold = []  
               
    def add_student(self,student):
        self.students[student.name] = student

    def register_student_for_placement(self,student):
        self.add_student(student)

    def process_placement(self,company_name,criteria):

        eligible_students = []
        for student_name, student in self.students.items():
            if eligible_students(criteria): 
                eligible_students.append(student_name)

            print(f"Eligible student for {company_name}: {','.join(eligible_students)}")

            if eligible_students:
                self.placed_students.append(eligible_students[0])
                print(f"{eligible_students[0]} is placed at {company_name}.")

            else:
                print("student is not eligible")

stud_1 = Placement("Ziyan", 8.74, 80, 70)
stud_2 = Placement("Ziya", 7, 60, 90)
stud_3 = Placement("Ram", 9, 90, 70)

Placement_System = Placementsystem()

Placement_System.register_student_for_placement(stud_1)
Placement_System.register_student_for_placement(stud_2)
Placement_System.register_student_for_placement(stud_3)

company_criteria = {"cgpa_criteria": 7.5, "attendence_criteria": 75}

Placement_System.process_placement("XYZ tech", company_criteria)



          
