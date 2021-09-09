import pytest

def test_proc():
    print("this is a test")
    num = not_a_test_proc() # setting the variable num to be the same as the output from the not a test program, which will be 1
    assert 1 == num

def not_a_test_proc():
    print("This is not a test")
    return 1                # returns 1

print(not_a_test_proc())
print(test_proc())

#then run python3 -m pytest in the console and it will run the test - does the assertation match the output?

#import classes_Dog

#def test_class():
    #testdog = classes_Dog.Dog
    #("testdog")
    #assert testdog.name == "testdog"

#def test_dogMod():
    #testdog = dogMod.dog("testdog")
    #assert testdog.speak("yipyipyip")

