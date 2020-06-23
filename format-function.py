'''
Format function
'''

users = ['Shadab', 'Aishah', 'Sadiq', 'Sufiya', 'Zaid', 'Pratibha', 'Aafiya']

computer = ['Raspberry pi', 'Dell Windows', 'Android', 'Macbook', 'Linux build', 'IOS', 'Sasta Computer']

# Naive Approach
# for i in range(0,len(users)):
#     print("computer Used By", users[i],"is",computer[i])

for i in range (0,len(users)):
    template = "Computer used by {} is {}"      # if want to change the order of list we have to specify the list index in {} i.e. Computer used by {1} is {0}
    print(template.format(users[i],computer[i]))