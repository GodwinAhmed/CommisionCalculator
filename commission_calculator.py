print("Welcome to the comissions calculator\n")

name = input(print("Please tell me your full name:"))
sales = int(input(print("Please tell me the total ZAR amout in sales made for the month:")))

commission = round(sales *13 /100, 2)

print(f"Hi {name}, your total commission based on sales you made is ZAR {commission}.")