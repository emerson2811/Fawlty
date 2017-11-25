try:
    def function1(a,b):
        print(a/b)

    function1(20,0)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This is going to execute no matter what happens")

