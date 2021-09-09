def gradeave(g1,g2,g3):
    return ((int(g1) + int(g2) + int(g3)) / 3)

def passfail(avgGradeIn):
    if avgGradeIn > 64:
        return 'passed'
    else:
        return 'failed'

with open("C:\\Users\\kdorm\\Documents\\QA academy\\python\\pythondfe\\20210909150916_6537.csv") as importedFile:
    importedData = importedFile.readlines()

importedData.remove(importedData[0])

print(importedData[0])

for i in importedData:
    templist = i.replace('"','')
    newlist = templist.rsplit(',')   # 0 is firstname, 1 is surname, 2 is email, 3 is grade1, 4 is grade2 5 is grade3
    avgGrade = gradeave(newlist[3],newlist[4],newlist[5])
    passState = passfail(avgGrade)
    certFileName = 'certsout\\' + newlist[0] + newlist[1] + '.html'
    certVar = '<!doctype html><html><head> <link rel="stylesheet" href="style.css"> </head><body>\n'
    certVar = certVar + f"<h1 class=\"title\">{newlist[0]} {newlist[1]}</h1>\n"
    certVar = certVar + f"<p> Your grades were as follows: </p>"
    certVar = certVar + f"<p class=\"grade\"> grade1: {newlist[3]} </p>"
    certVar = certVar + f"<p class=\"grade\"> grade2 {newlist[4]} </p>"
    certVar = certVar + f"<p class=\"grade\"> grade3 {newlist[5]} </p>"
    certVar = certVar + f"<p class=\"grade\"> average grade {avgGrade} </p>"
    certVar = certVar + f"<p class=\"pass\"> You have {passState} </p>"
    certVar = certVar + f"<p class=\"certedby\"> Certified by: Katie Diggory</p></body></html>"

    with open(certFileName,'w') as writeCert:
        writeCert.write(certVar)
    print(f"Written {certFileName}")