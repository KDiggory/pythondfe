def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

var = fact(5)
var2 = fact(2)

print(var)
print(var2)

