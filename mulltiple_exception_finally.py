try:
    open("this.txt","r")
except EOFError as e:
    print("EOF Error!")
except IOError as e:
    print("IO Error!")
finally:
    print("This will Always run irrespective of any exception")