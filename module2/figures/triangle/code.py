def triangle_perimeter(a, b, c):
    if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
        print("Периметр треугольника =", a + b + c)
    else:
        print("Такого треугольника не существует")
        
def triangle_area(a, b, c):
    if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
        p_per = (a + b + c) / 2
        s = (p_per * (p_per - a) * (p_per - b) * (p_per - c)) ** 0.5
        print("Площадь треугольника =", s)
    else:
        print("Такого треугольника не существует")