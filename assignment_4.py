#ex1

class Bike:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.speed = 0

    def accelerate(self, increment):
        self.speed += increment

    def brake(self, decrement):
        self.speed -= decrement
        if self.speed < 0:
            return "Odometer fault"
        else:
            return "No acceleration"

    def __str__(self):
        return f"{self.color} {self.brand} {self.model} going at {self.speed} km/h"


# Example usage:
my_bike = Bike("Yamaha", "R15 V4", "RED")
print(my_bike)  

my_bike.accelerate(15)
print(my_bike)  

my_bike.brake(5)
print(my_bike)  

my_bike.brake(20)
print(my_bike)  


#ex 2
class Student:
    def __init__(self,name):
        self.name = name
        self.attendance = 0
        self.marks = {}

    def mark_attendance(self,status):
        if status == "present":
            self.attendance += 1

        elif status == "absent":
            self.attendance -= 1

            if self.attendance < 0:
                self.attendance = 0

        else:
            return "Invalid attendance status.Mark 'present' or 'absent'."
        
    def get_attendance(self):
        return self.attendance
    
#ex 3
    def score(self,mark):
        if mark >=90 and mark <=100:
            return "A"
        elif mark >=80:
            return "B"
        elif mark >=70:
            return "C"
        elif mark >=60:
            return "D"
        else:
            return "F"
    
    def get_marks(self):
        return self.marks

      
#example
student_1 = Student("Ram")
student_1.mark_attendance("present")
student_1.mark_attendance("present")
student_1.score(86)

student_2 = Student("Jaanu")
student_2.mark_attendance("absent")
student_2.mark_attendance("present")
student_2.score(40)

print(f"{student_1.name} has attended {student_1.get_attendance()} classes and scored {student_1.get_marks()} grade.")
print(f"{student_2.name} has attended {student_2.get_attendance()} classes and scored {student_2.get_marks()} grade.")



#ex 4 
class Onlineorder:
    def __init__(self,order_id,cust_id,price,status):
        self.order_id = order_id
        self.cust_id = cust_id
        self.price = price
        self.status = status

    def update_status(self,new_status):
        self.status = new_status

    def display_order(self):
        print(f"order_id: {self.order_id}")
        print(f"cust_id: {self.cust_id}")
        print(f"price: ${self.price}")
        print(f"status: {self.status}")


order= Onlineorder(order_id=54367853,cust_id=0567468940,price=1500)
order.display_order(order)
order.display_order("Shipped")