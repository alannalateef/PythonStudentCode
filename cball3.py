# cball3.py
from math import pi, sin, cos, radians
class Projectile:
    def __init__(self, angle, velocity):
        self.xpos = 0
        self.ypos = 0
        theta = radians(angle)  # temporary variable
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)
    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time  # temporary variable
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1
    def getY(self):
        return self.ypos
    def getX(self):
        return self.xpos

def main():
    angle, vel, time = getInputs()
    cball = Projectile(angle, vel)
    while cball.getY() >= 0:
        cball.update(time)
        print("(xpos,ypos): ({},{})".format(cball.xpos,cball.ypos))
        
def getInputs():
    a = eval(input("Enter the launch angle (in degrees):"))
    v = eval(input("Enter the initial velocity (in meters/sec):"))
    t = eval(input("Enter time interval between calculations:"))
    return a,v,t

if __name__ == "__main__": 
    main()
