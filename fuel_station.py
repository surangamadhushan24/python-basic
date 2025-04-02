while True:
    number_of_liters = int(input("Enter number of Liters: "))

    if number_of_liters == -1:
        break

    customer_name = input("Enter customer name: ")
    fuel_price_per_liter = int(input("Enter fuel price per liter: "))

    if number_of_liters > 100:
        amount= fuel_price_per_liter * number_of_liters
        discount = amount * 0.12
    elif 50 <= number_of_liters < 100:
        amount = fuel_price_per_liter * number_of_liters
        discount = amount * 0.08
    elif 20 <= number_of_liters < 50:
        amount = fuel_price_per_liter * number_of_liters
        discount = amount * 0.05
    else:
        amount = fuel_price_per_liter * number_of_liters
        discount = 0

    print(amount + discount)
    print(customer_name)
    print(number_of_liters)
    print(f"the number of liters is {number_of_liters}")
