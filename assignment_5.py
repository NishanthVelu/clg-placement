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



    