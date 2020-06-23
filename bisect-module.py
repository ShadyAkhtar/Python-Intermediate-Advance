import bisect

# Bisect module should be used on sorted list

list1 = [1,2,35,4,6,7,8,9,34]

number = 5

print(bisect.bisect(list1, number))     #It return the index where the require element can be placed

bisect.insort(list1,number)         #Insert in the list at appropriate position

print(list1)