list1 = ['Chalk', 'duster', 'board', 'pen']

# naive approach

# for item in list1:
#     if item is not 'pen':
#         print(item, "and ", end="")
#     else:
#         print(item)

#Join Function
print(" and ".join(list1))