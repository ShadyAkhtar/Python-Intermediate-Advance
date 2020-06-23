''' 
List Comprehension
Dictionary Comprehension
Set Comprehension
Generator Comprehension
'''

list_1 = [12,23,45,67,8,9,343,55,66,88,12,34,90,112,114,145]
divide_by_3 = []
for item in list_1:
    if item%3 == 0:
        divide_by_3.append(item)
print("Without using list comprehension : ",divide_by_3)
print("Using list comprehension : ",[item for item in list_1 if item%3 == 0])

#Dictionary
dict1 = {"a":45, "b":65, "A":5}
print({k.lower():dict1.get(k.lower(),0)+dict1.get(k.upper(),0) for k in dict1.keys()})

#Set
squared = {x**2 for x in [1,2,3,3,4,4,4,5,5,5,5,6,6,7]}
print(squared)

#generator
gen = (i for i in range(56) if i%3==0)
for item in gen:
    print(item)