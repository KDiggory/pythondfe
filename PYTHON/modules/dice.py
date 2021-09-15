def dice_roll():
    import random
    number = random.randint(1,6)
    number2 = random.randint(1,6)
    return number, number2
   


def d10():
    import random
    number = random.randint(1,10)
    return number

def d20():
    import random
    number = random.randint(1,20)
    return number


six = dice_roll()
print(six)
twenty = d20()
print(twenty)
