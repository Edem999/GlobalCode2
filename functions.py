# def hello():
#     print("hello")
# def goodbye():
#     print("Goodbye")
# def NameSchool():
#     print("HTU")   

# hello()
# goodbye()
# NameSchool()

# def addition(num1,num2):
    
#     print(num1 + num2)
# numa = int(input("Enter the first number: "))
# numb = int(input("Enter the second number: "))
# addition(numa,numb)    

def traffic(var):
    if var.upper() == "RED":
        print("stop")
    elif var.upper() == "YELLOW":
        print("get ready")
    elif var.upper()=="GREEN":
        print("go go go and go")
valuet = input("Enter the traffic light color: ")
traffic(valuet)