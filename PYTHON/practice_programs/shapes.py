# create class and subclass objects which represent different geometrical shapes such as rectangele and squarec
# worked well until adding the superclass :( 
import math

class shapes():
    #def __init__(self):
        #self.dim = dim
        #print("2D or 3D? Type 2 or 3 please: ")
        #self.dim = dim
        #self.dim = input(">")
    def dimen(self):
        print("2D or 3D? Type 2 or 3 please: ")
        self.dim = int(input(">"))
        return self.dim

class square(shapes):
    def __init__(self, sideLen):
        self.sideLen = sideLen
        self.dim = shapes.dimen(self)

    def sq_area(self):
        if self.dim == 2: 
            area_sq = self.sideLen * self.sideLen
            return area_sq  
        elif self.dim == 3:
            area_sq = self.sideLen * self.sideLen * self.sideLen
            return area_sq
        else:
            print("I can only calculate 2D or 3D area unfortunately")



class rectangle:
    def __init__(self, sideLen1, sideLen2):
        self.sideLen1 = sideLen1
        self.sideLen2 = sideLen2
        self.dim = shapes.dimen(self)

    def rec_area(self):
        if self.dim == 2:
            area_rec = self.sideLen1 * self.sideLen2
            return area_rec
        elif self.dim == 3:
            print("What is the depth of your 3d rectangle?")
            depth = float(input(">"))
            area_rec = self.sideLen1 * self.sideLen2 * depth
            return area_rec
        else:
            print("I can only calculate 2D or 3D area unfortunately")
            


class triangle:
    def __init__(self, height, base):
        self.height = height
        self.base = base
        self.dim = shapes.dimen(self)

    def tri_area(self):
        if self.dim == 2:
            area_tri = (self.height * self.base)/2
            return area_tri  
        elif self.dim == 3:
            print("What is the depth of your 3d rectangle?")
            depth = float(input(">"))
            area_tri = (self.height * self.base)/2
            area_tri3D = area_tri * depth
            return area_tri3D


class circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = math.pi
        self.dim = shapes.dimen(self)

    def cir_area(self):
        if self.dim == 2:
            area_cir = self.pi * (self.radius ** 2)
            return area_cir 
        elif self.dim == 3:
           area_cir =  4/3*self.pi * self.radius**3
           return area_cir


#square_test = square(15)  ## dont need to call the superclass, the subclass inherits anyway, doesnt need calling
##square_test = square_test.sq_area()
#print(square_test)

rectangle_test = rectangle(1,2)
rectangle_test = rectangle_test.rec_area()
print(rectangle_test)

#circle_test = circle(2)
#circle_test = circle_test.cir_area()
#print(circle_test)

#tri_test = triangle(2,3)
#tri_test = tri_test.tri_area()
#print(tri_test)




