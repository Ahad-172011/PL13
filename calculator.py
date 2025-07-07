def add(d, f):
               print((d, '+', f, '=', d + f))
def subtract(d, f):
               print((d, '-', f, '=', d - f))
def multiply(d, f):
               print((d, '*', f, '=', d * f))
def divide(d, f):
               print((d, '/', f, '=', d / f))


op = input("enter your choice")

print("a. add")
print("b. subtract")
print("c. multiply")
print("d. divide")

a = int(input("enter your first num"))
b = int(input("enter your second num"))

if op == 'add':
    add(a, b)
elif op == 'subtract':
    subtract(a, b)
elif op == 'multiply':
    multiply(a, b)
elif op == 'divide':
    divide(a, b)
else:
    print("Invalid ")