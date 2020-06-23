a = ['Shadab' , 'Aishah' , 'Sadiq' , 'Sufiya' , 'Zaid' , 'Pratibha' , 'aafiya']

# Naive Approach
# i=0
# for item in a:
#     i = i+1
#     if i%2==0:
#         print(item)

# Enumerate Function
for i, item in enumerate(a):
    if (i+1)%2==0:
        print(item)