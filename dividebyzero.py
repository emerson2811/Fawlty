
def zerodivider(numerator,denominator):
    try:
        return a/b
    except ZeroDivisionError:
        print("You cannot divide by zero")
        return 0

x = float(input('Enter a number'))
y = float(input('Enter value by which you want to divide the number'))
result = zerodivider(x,y)
print(result)
