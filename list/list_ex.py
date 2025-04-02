numbers = [12, 45, 7, 32, 18]

max = numbers[0]
min = numbers[1]

for number in numbers:
    if max < number:
        max = number

    if min > number:
        min = number

print(f"max value is {max} min value is {min}")
