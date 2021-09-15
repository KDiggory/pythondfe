#file = open("C:\\Users\\kdorm\\Documents\\QA academy\\python\\pythondfe\\Files\\Filename2.txt", "w")
#file2 = open("C:\\Users\\kdorm\\Documents\\QA academy\\python\\pythondfe\\Files\\Filename3.txt", "w")

file1 = open("C:\\Users\\kdorm\\Documents\\QA academy\\python\\pythondfe\\Files\\Filename2.txt")
file2 = open("C:\\Users\\kdorm\\Documents\\QA academy\\python\\pythondfe\\Files\\Filename3.txt", "w")
file2.write("\nThis is a new line\n")
    #for line in file1:
        #file2.write(line)
file1.close()
file2.close()

readoriginal = open("C:\\Users\\kdorm\\Documents\\QA academy\\python\\pythondfe\\Files\\Filename2.txt", "r")
readnew = open("C:\\Users\\kdorm\\Documents\\QA academy\\python\\pythondfe\\Files\\Filename3.txt", "r")

linesorig = readoriginal.readlines()
linesnew = readnew.readlines()
print(linesorig)
print(linesnew)

readoriginal.close()
readnew.close()

appendonto = open("C:\\Users\\kdorm\\Documents\\QA academy\\python\\pythondfe\\Files\\Filename3.txt", "a+")
tobeappended = open("C:\\Users\\kdorm\\Documents\\QA academy\\python\\pythondfe\\Files\\Filename2.txt", "r")

appendonto.write(tobeappended.read())

appendonto.seek(0)
tobeappended.seek(0)

print('content of new file after appending -', appendonto.read())
print('content of original file after appending -\n', tobeappended.read())

appendonto.close()
tobeappended.close()


