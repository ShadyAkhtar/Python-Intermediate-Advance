list1 = [3,4,5,8,9,7,6,12,14,15,16,52,24]
# No. of elemnt : 5-3 = 2 # [3:5]
print(list1[2:5])
print(list1[:5])
print(list1[5:])
print(list1[2:-5])  #count index backtrack from end of the list
print(list1[-2:-5]) #invalid it should be [-5:-2] Hint : Just to remember, first value should be greater in terms of number
print(list1[-5:-2])

print(list1[::1])   #print as it is
print(list1[::2])   #print list by skipping 1 element
print(list1[::3])   #print list by skipping 2 elements
print(list1[::-1])  #print list in reverse order
print(list1[::-2])  #print element in reverse by skipping one element
print(list1[::-3])  #print element in reverse by skipping two element