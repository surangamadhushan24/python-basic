
list_of_tuples = [(1, 2), (3, 4), (5, 6)]

# max = sum(list_of_tuples[0])
# maxtuple =()
# for i in list_of_tuples:
#     if max < sum(i):
#         maxtuple = i
#
# print(maxtuple)

max_tuple = max(list_of_tuples,key=sum)
print(max_tuple)
