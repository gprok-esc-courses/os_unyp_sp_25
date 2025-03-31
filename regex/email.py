import re 

pattern = '^[A-Za-z0-9]+(\.[A-Za-z0-9]+)*@[A-Za-z0-9]+(\.[A-Za-z0-9])*\.[A-Za-z]{2,4}$'
email = input("Your email: ")

correct = re.match(pattern, email)

if correct:
    print("Email accepted")
else:
    print("Wrong email")

