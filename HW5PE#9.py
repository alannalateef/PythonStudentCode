
import math

class Sphere:
     
    def __init__(self,radius): #Creates sphere having given radius
        self.radius = radius
         
    def getRadius(self): #Returns the radius of this sphere
        return self.radius
     
    def surfaceArea(self): #returns surface area of sphere
        return 4*math.pi*(self.radius**2)
     
    def volume(self): #returns volume of sphere
        return (4/3)*math.pi*(self.radius**3)

def Main():
    s = eval(input("Enter radius of Sphere "))
    sp = Sphere(s)  #sets radius to input value
    print("sphere sp radius=", sp.getRadius()) #prints outputs devired from the class
    print("surface area=", sp.surfaceArea())
    print("volume=", sp.volume())

Main()
