fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]

# count = 0;
# for fruit in fruits:
#     if fruit.lower() == "apple":
#         count += 1
#
#
# print(f"{count} apples in list")

fcount = [fruit.lower() for fruit in fruits].count("apple")
print(fcount)
