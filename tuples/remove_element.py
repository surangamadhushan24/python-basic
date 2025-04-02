my_tuple = (1, 2, 3, 4, 5)
new_tuple = tuple(x for x in my_tuple if x != 3)
print(new_tuple)
