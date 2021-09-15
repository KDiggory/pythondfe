from abc import ABC, abstractmethod

class bird(ABC):            ## the ABC means that you can't create an instance of bird without a subclass of breed. This is a template only
    fly = True
    babies = 0

    def noise(self):
        return("Squawk")

    def reproduce(self):
        self.babies += 1
        return self.babies

    def mortality(self):
        self.mort = self.babies/2
        return self.mort

    @abstractmethod         ## abstraction allows us to create the lowest level blueprint of a class without anyone being able to make an instance without doing this
    def eat(self):          ## in all the classes that inherit from bird you have to override the @abstractmethod decorator
        pass                

    extinct = False


class Owl(bird):                    # inheritance used to create the child class of bird
    def reproduce(self):
        self.babies += 6            # polymorphism is used to override the reproduce method
        return f"{self.babies} owlets \U0001F970"

    def eat(self):                  
        return "Peck Peck"          # abstraction with the eat method

    def mortality(self):
        if not self.extinct:
            self.mort = (self.babies/2)/self.babies *100 
            return f"{self.mort}% mortality"

class Dodo(bird):                   # inheritance used to create the child class of bird
    fly = False                     # polymorphism to override the fly and extinct variables
    extinct = True

    def eat(self):
        return "nom nom"
        
    def reproduce(self):
        if not self.extinct:        # encapsulation to keep the babies variable from being directly accessed
            self.babies += 1
            return self.babies
        if self.extinct:
            return f"dodos are extinct, they don't have any babies"

    def mortality(self):
        if not self.extinct:
            self.mort = (self.babies/2)/self.babies *100 
            return self.mort
        if self.extinct:
            return f"dodos are extinct, so mortality rates dont apply!"


owl = Owl()
owlbabies = owl.reproduce()
owleat = owl.eat()
owlbabymortality = owl.mortality()
#print(owlbabies) ## this returns 6 
#print(owleat)
#print(owlbabymortality)
print(f"Owls bave an average of {owlbabies}, they say {owleat} when they are eating. Sadly there is a {owlbabymortality} rate \U0001F62D")

dodo = Dodo()
dodobabies = dodo.reproduce()
print(dodobabies)  ## this returns none as the self.babies variable is not accessible due to encapsulation

#test = bird()       ## TypeError: Can't instantiate abstract class bird with abstract method eat --> because of the @abstractionmethod for eat