file = open("C:\\Users\\kdorm\\Documents\\QA academy\\python\\pythondfe\\Files\\Filename2.txt", "w")
file.write("Malton football club")
file.write("\nSwinton rugby club")
file.write("\nBroughton darts association")
file.write("\nAmotherby bowls team")
file.write("\nNorton handball club\n")
#for n in range(1,6):
    #newline = "Team: " + str(n) + "\n"
    #file.write(newline)

file.close()

file = open("C:\\Users\\kdorm\\Documents\\QA academy\\python\\pythondfe\\Files\\Filename2.txt", "r")
outfile = ""

for line in range(1,6):
    if line == 1:
        outfile += file.readline()
    elif line == 4:
        outfile += file.readline()
    else:
        file.readline()

print(outfile)
file.close()





