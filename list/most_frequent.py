from collections import Counter


numbers = [1, 3, 2, 3, 4, 3, 5]

frequencies = Counter(numbers)

item,frue = frequencies.most_common(1)[0]
print(item)










