#email = "katiediggory@gmail.com"
#print(email.split("@"))

def splitting():
    useremail = str(input("What is your email address? "))
    if "@" in useremail: 
        splitemail = useremail.split("@")
        name = splitemail[0]
        domain = splitemail[1]
        print(f"Hello {name}, you have a {domain} email ")
    else:
        print("Thats not a valid email, try again")
        splitting()


splitting()

