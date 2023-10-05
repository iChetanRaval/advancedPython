
a = 5
b = 2

try:
    print("Resource open")
    print(a/b)
    k = int(input("Enter a number: "))
    print(k)

except ZeroDivisionError as e:  # as e => is for if error is occured then it print what is error
    print("Hey, You cannot divide a Number by Zero",e)
except ValueError as e:
    print("Invalid Input",e)

except Exception as e:
    print("Something went wrong",e)

finally:   # => it will execute even if there is an error
    print("Resource Closed")
