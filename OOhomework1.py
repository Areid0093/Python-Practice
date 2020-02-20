import math

class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coordinate1
        self.coor2 = coordinate2

    def distance(self):
        print(math.sqrt((self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2))

    def slope(self):
        print((self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0]))
        

coordinate1 = (3,2)
coordinate2 = (8,10)

class Cylinder:
    
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
    
    def volume(self):
        print(round(math.pi*(self.radius**2)*self.height, 2))
        
    def surface_area(self):
        print(round((2*math.pi*self.radius*self.height) + (2*math.pi*(self.radius**2)), 2))
    
c = Cylinder(2,3)