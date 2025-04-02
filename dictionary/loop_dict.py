person = {"name ": "bob", "age": 30, "city": "tokyo"}

for key in person:
    print(key)

for key,value in person.items():
    print(f"{key}: {value}")
    

for key in person:
    print(person[key])