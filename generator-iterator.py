'''
Iterable
Iterator
Iteration
''' 

# it uses more resources on run time
# for i in range(100000):
#     print(i)

#Generator will store the information in object instead of using resources on runtime


def gen(n):
    for i in range(n):
        yield i

# print(gen(100000))

# for i in gen(1000):
#     print(i)


ob1 = gen(4)
print(next(ob1))
print(next(ob1))
print(next(ob1))
print(next(ob1))

print("*******************************************")
num="ABCDEF"
iter1=iter(num)
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))