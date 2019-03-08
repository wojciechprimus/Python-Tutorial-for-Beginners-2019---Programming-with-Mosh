good_credit=True
price=1000000
if good_credit:
    print("They need to put down 10%")
    price=price*0.1
else:
    print("They need to put down 20%")
    price=price*0.2

print(f"Down payment is now: {price}$ ")
