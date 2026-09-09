
users = {
    "JOEL" : "eatfood",
    "EMMA" :"godisgood",
    "GINA" : "afflu"
}
user=input("enter your username: ").upper()
password=input("enter your password: ")

if users[user] == password:
    print("login succesful")
else :
    print("login failed")