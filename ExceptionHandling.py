a = 5
b = 0


try:
    print(a/b)
    print("Hiiii")

except ZeroDivisionError as e:
    print("Division by zero not Allowed", e)
try:
    k = int(input("Enter Number"))
    print(k)
except ValueError:
    print("Provide Number")

finally:
    print("Bye Macha")
