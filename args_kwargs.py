# *args and **kwargs tutorials
# *vars and **kvars tutorial



# *args demo


def function_1(*args):
    print(type(args))
    if (len(args)==3):
        print("The Name Of the Student is", args[0], "and the age is", args[1], "and rollno is", args[2])
    else:
        print("The Name Of the Student is", args[0], "and the age is", args[1])

def printmarks(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print("Name : ",key,"-- Marks : ", value) 

def master(normal, *args, **kwargs):
    print(normal)
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print("Name : ",key,"-- Marks : ", value)
    


# printing *args 
print("************************************************************************************************")
function_1("Shadab", 22)

lis=["Shadab", 22, 18001]
function_1(*lis)
print("************************************************************************************************")

print("************************************************************************************************")

marks = {"Shadab":85, "Sadiq":75, "Zaid":70, "Aishah":80, "Pratibha":65, "Sufiya":70}
printmarks(**marks)

print("************************************************************************************************")


print("************************************************************************************************")
print("master")
master("Normal Text", *lis, **marks)
print("************************************************************************************************")

