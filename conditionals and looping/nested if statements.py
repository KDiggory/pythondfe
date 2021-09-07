bookData = {"been read":False, "pages":100, "title":"concrete pouring"}

if bookData["been read"]: ## can just use if when working with booleans as if checks whether something is true or false
    if bookData["pages"] > 200:
        print(bookData["title"] + " is a long book")
    else:
        print(bookData["title"] + " is a short book")
else:
    print("I have not read" + bookData["title"])

