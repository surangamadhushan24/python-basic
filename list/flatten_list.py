list_of_lists = [[1, 2], [3, 4], [5, 6]]

# all_numbers = []
#
# for i in list_of_lists:
#     for j in i:
#         all_numbers.append(j)
#
# print(all_numbers)

flatten_list = [x for sub in list_of_lists for x in sub]
print(flatten_list)
