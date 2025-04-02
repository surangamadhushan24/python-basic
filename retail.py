

amount = float(input("enter your purchase amount "))


if amount >= 5000:
    points = 50

elif 4999 >= amount >= 3000:
    points = 30

elif 2999 >= amount >= 1000:
    points = 10
else:
    points = 0

print(amount, points)


