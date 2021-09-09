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
        self.dim = 0
        self.dim = int(input(">"))

class square(shapes):
    def __init__(self, sideLen, dim):
        self.sideLen = sideLen
        self.dim = 2
        self.dim = shapes.dimen(self)

    def sq_area(self):
        if self.dim == 2: ## this line is giving me issues
            area_sq = self.sideLen * self.sideLen
            return area_sq  
        elif self.dim == 3:
            area_sq = self.sideLen ** self.sideLen 
            return area_sq
        else:
            print("I can only calculate 2D or 3D area unfortunately")



class rectangle:
    def __init__(self, sideLen1, sideLen2):
        self.sideLen1 = sideLen1
        self.sideLen2 = sideLen2

    def rec_area(self):
        area_rec = self.sideLen1 * self.sideLen2
        return area_rec  


class triangle:
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def tri_area(self):
        area_tri = (self.height * self.base)/2
        return area_tri  


class circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = math.pi

    def cir_area(self):
        area_cir = self.pi * (self.radius ** 2)
        return area_cir 

#test = triangle(1,2) ## create the class
#tritest = test.tri_area()
#print(tritest) # comes out as one, which is right

#testsq = square(5, dim=2)
testsh = square(5,2)  ## dont need to call the superclass, the subclass inherits anyway, doesnt need calling
testsh2 = testsh.sq_area()
print(testsh2)
#help(testsh)
#sqtest = testsq.sq_area()#
#sqtest3 = testsq.sq_area()
#print(sqtest3) # comes out as 25 which is right

#testrec = rectangle(5, 9)
#rectest = testrec.rec_area()
#print(rectest) # comes out as 45 which is right

#testcir = circle(5)
#cirtest = testcir.cir_area()
#cirtest = round(cirtest, 2)
#print(cirtest) # comes out as 78.5398.... which is right, changed to 2 decimal places using round()



