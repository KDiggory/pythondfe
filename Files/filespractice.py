import pdb
pdb.set_trace()


def gradeavg(g1,g2,g3):
    return ((int(g1) + int(g2) + int(g3)) / 3)

def passFail(avgGradeIn):
    if avgGradeIn > 59:
        return "Pass"
    else:
        return "Fail"



with open("C:\\Users\\kdorm\\Documents\\QA academy\\python\\pythondfe\\20210909150916_6537.csv") as importedFile:    # 20210909150916_6537.csv
        importedData = importedFile.readlines() # gives the file as data in lines
print(importedData[0])  # prints the headings of each column

# need to remove the headings because they arent integers so cant be added for the average!
importedData.remove(importedData[0])
print(importedData[0])

for i in importedData:
        #print(i)    ## prints the information in lines
    tempList = i.replace('""', '') 
    separatedList = i.rsplit(",") # separates the data in the list by comma - done on each line which is why you use readlines earlier
    #print(separatedList[0] + " " + separatedList[1]) # 0 = firstname 1 = surname 2 = email 3 = grade1 4 = grade2 5 = grade3
    avgGrade = gradeavg(separatedList[3],separatedList[4],separatedList[5])
    passState = passFail(avgGrade)
    certFileName = "certsOut\\" + separatedList[0] + separatedList[1] + ".html "
    #print(separatedList[0] + "Average grade" + str(avgGrade) + "you have a: " + passFail(avgGrade))
    certVar = '<!docttype html><html><head> <link rel="stylesheet" href="style.css"> </head>\n'
    certVar = f"<h1>{separatedList[0]}{separatedList[1]}</h1>\n"
    certVar = certVar + f"<h1 class=\"title\">{separatedList[0]} {separatedList[1]}</h1>\n"
    certVar = certVar + f"<p> Your grades were as follows: <p>"
    certVar = certVar + f"<p class=\"grade\" > grade1 {separatedList[3]}</p>"
    certVar = certVar + f"<p class=\"grade\" > grade2 {separatedList[4]}</p>"
    certVar = certVar + f"<p class=\"grade\" > grade3 {separatedList[5]}</p>"
    certVar = certVar + f"<p class=\"grade\" > average grade  {avgGrade}</p>"
    certVar = certVar + f"<p class=\"pass\" > you have a  {passState}</p>"

    with open(certFileName, "w") as writeCert:
        writeCert.write(certFileName)
        print(f"Written {certFileName}")



    
    
    
    
    
    
    
           
   ## could make it as a dictionary - try and do this later
   # for j in separatedList:
        # studentDict =       
 
