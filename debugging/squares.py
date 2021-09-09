def list_of_squares(n):
    d=dict()
    for i in range(1,n+1):
        d[i]=i*i
    return d

var = list_of_squares(5)
print(var)