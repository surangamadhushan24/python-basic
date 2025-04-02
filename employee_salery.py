base_salary = float(input("Enter your base salary: "))
experience = float(input("Enter your experience years: "))
performance_rating = float(input("Enter your performance ratings: "))

if experience >= 10:
    if performance_rating == 5:
        bonus = base_salary * 0.2
        full_payment = base_salary + bonus
        print(bonus, full_payment)

    elif performance_rating == 4:
        bonus = base_salary * 0.15
        full_payment = base_salary + bonus
        print(bonus, full_payment)

    else:
        bonus = base_salary * 0.1
        full_payment = base_salary + bonus
        print(bonus, full_payment)

elif 5 < experience < 10:
    if performance_rating == 5:
        bonus = base_salary * 0.15
        full_payment = base_salary + bonus
        print(bonus, full_payment)

    elif performance_rating == 4:
        bonus = base_salary * 0.1
        full_payment = base_salary + bonus
        print(bonus, full_payment)

    else:
        bonus = base_salary * 0.05
        full_payment = base_salary + bonus
        print(bonus, full_payment)

else:
    if performance_rating == 5:
        bonus = base_salary * 0.1
        full_payment = base_salary + bonus
        print(bonus, full_payment)

    elif performance_rating == 4:
        bonus = base_salary * 0.05
        full_payment = base_salary + bonus
        print(bonus, full_payment)

    else:
        bonus = 0
        full_payment = base_salary + bonus
        print(bonus, full_payment)




