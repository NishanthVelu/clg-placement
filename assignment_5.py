#travelling

class Travelling:
     
    def __init__(self,destination,route,SaftyGears,accomodation,budget):
        self.destination = destination
        self.route = route
        self.SaftyGears = SaftyGears
        self.accomodation = accomodation
        self.budget = budget

    def PlanTrip(self):
        print("Planning bike trip to:",self.destination)
        print("1. route:",self.route)
        print("2. accomodation:",self.accomodation)
        print("3. Safty Precautions:",self.SaftyGears)
        print("4. Total budget estimation:",self.budget)

destination = "Ladakh"
route = "By Road from Tamil Nadu - vellore to Ladakh "
SaftyGears = "Helmet, Riding Jacket, Boots, Glows, Thermal Liner "
accomodation = "campimg along the way"
budget = "The estimated budget for the trip is 4 lakhs"

TripPlan = Travelling(destination, route, SaftyGears, accomodation, budget)
TripPlan.PlanTrip()



class Destinations():
    def __init__(self,staring_point):
        self.stating_point = staring_point
        self.destinations = []

    def AddDestination(self,destination):
        self.destinations.append(destination)

    def StartTrip(self):
        print("Staring bike trip from", self.stating_point)

        for i in range(len(self.destinations) - 1):
            print("Biking from", self.destinations[i], "to" ,self.destinations[i+1])
        print("The final destination gonna be ", self.destinations[-1])


trip = Destinations("Vellore")
trip.AddDestination("Kerala")
trip.AddDestination("Karnataka")
trip.AddDestination("Andhra Pradesh")
trip.AddDestination("Odisha")
trip.AddDestination("West Bengal")
trip.AddDestination("Uttar Pradesh")
trip.AddDestination("Rajasthan")
trip.AddDestination("Delhi")
trip.AddDestination("Jammu Kashmir")
trip.AddDestination("Ladakh")

trip.StartTrip()



from bs4 import BeautifulSoup

soup = BeautifulSoup(flipcart.html, 'html.parser')

def finf_name():
    print(soup.text, "soup text")
    product_name = soup.find(class_="span.B_NuCI")
    product_price = soup.find(class_="div._30jeq3._16JK6d")

    print(product_name,product_price)





class plan_1:

    def __init__(self):
        self.starting_point = ""
        self.destination_1 = ""
        self.duration = ""
        self.activities = []

    def set_starting_point(self,starting_point):
        self.starting_point = starting_point

    def set_destination_1(self,destination_1):
        self.destination_1 = destination_1

    def set_duration(self,duration):
        self.duration = duration

    def set_activity(self,activity):
        self.activities.append(activity)

    def plan_trip(self):
        print("staring the trip from:",self.starting_point)
        print("Heading towards", self.destination_1)
        print("Duration to reach ",self.destination_1, "is", self.duration)
        print("Activities to perform:")
        for i, activity in enumerate(self.activities, 1):
            print(f"{i}. {activity}")

trip = plan_1()
trip.set_starting_point("Vellore")
trip.set_destination_1("Kerala")
trip.set_duration("4 days")
trip.set_activity("Varkala beach ride and resort stay")
trip.set_activity("kochin wonderla")
trip.set_activity("munnar-echo points,koluku maalai sun rise view")
trip.set_activity("munnar-tea estate,gap road")

trip.plan_trip()



class Heading_Destination_1:
    def __init__(self,rooms,price,rating):
        self.rooms = rooms
        self.price = price
        self.rating = rating 
        self.wonderla_rides = []

    print("Came to Kerala and make the planned activities quick and safe")

    def Room_Stay(self):
        if self.price <= 500 and self.rating >= 4.5:
            return "Affordable and book it."
        
        elif self.price > 500 and self.rating < 4.5:
            return "Affordable and think about it."
        
        else:
            return "Not suitable for stay"

room1 = Heading_Destination_1("Abc rooms",490,4.6)
room2 = Heading_Destination_1("Cdf rooms",700,3)

print("room 1:", room1.Room_Stay())
print("Room 2:", room2.Room_Stay())

        

class D_1_Activities():

    def __init__(self, weather):
        self.weather = weather
        

    def Choose_Activities(self):
        activities = []

        if self.weather == "sunny":
            activities.append("Bike Ride")
            activities.append("HIking")
            activities.append("Trecking")

        elif self.weather == "Rainy":
            activities.append("Indoor Campfire")
            activities.append("Rain Ride")

        return activities
    
plan = D_1_Activities("sunny")

print("Activities for sunny weather :", plan.Choose_Activities())



class Wonderla():
    def __init__(self,perference):
        self.preference = perference

    def wonderla_activities(self):
        
        if self.preference == "water":
            print("If the plan is on water try rides like surfing , slidding etc.")

        elif self.preference == "Non water":
            print("If the plan is on non water try rides like gaint wheel,car dash etc.")

        else:
            print("Don't wate time move on.")

activity = Wonderla("water")

activity.wonderla_activities()

        
            
            

        


         

    




    