tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3, 4, 5)

is_sub_set = set(tuple1).issubset(set(tuple2))
print("yes" if is_sub_set == True else  "NO")
print(is_sub_set)


