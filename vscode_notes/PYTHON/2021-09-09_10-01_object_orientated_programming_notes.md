:There are two main types of programming:
Procedural
programming comes from a history of being a list of things to do in order -> this is a procedural programming language. eg, basic. Statements must be in order, 
and are a list of commands. 
Procedural programming languages end up with very large monolithic blocks of code

Object Oriented 
More abstraction than procedural. 
OOP was writtten to break out of the paradigm that you needed to write procedurally. We want to work with discrete things we can inherit into more complex things
basically modularise the code more than you could with procedural programming languages. 

To facilitate this:

Inheritance - One object acquires all the properties and behaviours of a parent object. Pulling out the useful parts to use, can add to them too. 
Polymorphism - performing a single action in different ways. The same function running, but different response for each subclass. 
                Overriding --> can over ride a method from the superclass in the subclass if you want a different outcome. Done by naming a class the same as the one in the parent
                Overloading -->  Can be done in most OOP but not python. It is where you have 2 methods with the same name but different signatures (arguments). The advantage vs overriding is it increases code readability and maintainability.
                Depending what kind of objects are on either side of a plus sign changes what the plus sign will do
                num1 = int(input(num1))
                num2 = int(input(num2))                 These two give different results - when the input are ints it add them together
                var = num1 + num1
                print(var)

                num1 = str(input(num1))                 This concatenates the two inputs as they are strings
                num2 = str(input(num2))
                var = num1 + num2
                print(var)


Abstraction - hiding the implementation details and show only the functionality to the user. may feel like repeating code, but means you force someone to have a particular function in the inheritance of the class

Encapsulation - wrapping code together and data together into a single unit for data integrity 
