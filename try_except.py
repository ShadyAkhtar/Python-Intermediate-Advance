try:
    open("this.txt")
except Exception as e:
    print(e)
print("After Exception")