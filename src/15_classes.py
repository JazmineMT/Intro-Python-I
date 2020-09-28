# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self , lat , lon):
     self.lat = lat
     self.lon = lon
    def location(self):
        print(f"My loction is latitiude:  {self.lat}°  and longitude: {self.lon}° ")
         


p1 = LatLon("34", "35")

p1.location()

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self , name , lat, lon):
        self.name = name
        super().__init__(lat, lon)

    def waypoint(self):
        print(self.name , self.lat, self.lon) 
    def __str__(self):
        return {'name':self.name, 'lat': self.lat , 'lon' :self.lon}       
           

p2 = Waypoint("Catacombs", "41.70505", "-121.51521")


p2.waypoint()

print(p2.__str__())

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method



# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        self.difficulty = difficulty 
        self.size = size
        super().__init__(name, lat, lon)
    def geocache(self):

        print(f"{self.name }, diff : {self.difficulty} , size:  {self.size }, {self.lat} , {self.lon}")

    def __str__(self):
        return {'name':self.name, 'difficulty':self.difficulty, 'size' : self.size , 'lat': self.lat , 'lon' :self.lon}    

p3 = Geocache("Newberry Views", 1.5, 2, "44.052137", "-121.41556")
p3.geocache()

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

# Print it--also make this print more nicely

print(p3.__str__())
