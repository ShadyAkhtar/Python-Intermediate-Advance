try:
    print("This is a simple statement")
    # open("this.txt")
except Exception  as e:
    print(e)
else:
    print("if no exception occur. This will execute, ***SUCCESS***")
finally:
    print("this will execute at always execute in all condition. ***FINALLY***")