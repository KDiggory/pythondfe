import pdb ## imports the debugging module

pdb.set_trace() ## this line will let you run through the code line by line

a = "aaa"
b = "bbb"
c = "ccc"

final = a + b + c
print(final)


a = "aaa"
b = "bbb"
c = "ccc"

def final(var1,var2,var3):
    pdb.set_trace()
    return(var1+var2+var3)

print(final(a,b,c))