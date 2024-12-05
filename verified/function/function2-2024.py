one = int(input("Введите первое число: "))
two = int(input("Введите второе число: "))
action = input("Введите операцию [+, -, *, /]: ")

def calc(a, b, operation):
    if operation == "+":
        return(a + b)
    elif operation == "-":
        return(a - b)
    elif operation == "*":
        return(a * b)
    elif operation == "/":
        return(a / b)
    else:
        return("Операция не поддерживается")

print(calc(one, two, action))
