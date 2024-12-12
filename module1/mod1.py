def max(a, b):
    if a > b:
        max = a
    else:
        max = b
    print("Максимум =", max)
    
def chetn(a, b):
    if a % 2 == 0:
        print("Первое число четное")
    else:
        print("Первое число нечетное")
    if b % 2 == 0:
        print("Второе число четное")
    else:
        print("Второе число нечетное")
        
def del5(a, b):
    if a % 5 == 0:
        print("Первое число делится на 5")
    else:
        print("Первое число не делится на 5")
    if b % 5 == 0:
        print("Второе число делится на 5")
    else:
        print("Второе число не делится на 5")
