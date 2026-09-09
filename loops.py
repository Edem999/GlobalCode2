price=[]
total =0
for i in range(3):
    price.append(float(input("enter the price :")))

for i in price:
    total += i

print("total:",total)
