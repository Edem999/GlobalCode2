# traffic = input("Enter the traffic light color: ")
# print()
# if traffic == "red" or "RED" or "Red":
#     print("stop")
# elif traffic == "yellow" or "YELLOW"or "Yellow":
#     print("get ready")
# elif traffic =="green" or "GREEN" or "Green":
#     print("go go go and go")

traffic = input("Enter the traffic light color: ")
print()
if traffic.upper() == "RED":
    print("stop")
elif traffic.upper() == "YELLOW":
    print("get ready")
elif traffic.upper()=="GREEN":
    print("go go go and go")