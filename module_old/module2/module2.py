from figures.triangle.code import *
from figures.square.code import *

t_a = int(input("Введите первую сторону треугольника: "))
t_b = int(input("Введите вторую сторону треугольника: "))
t_c = int(input("Введите третью сторону треугольника: "))

s_a = int(input("Введите сторону квадрата: "))

triangle_perimeter(t_a, t_b, t_c)
triangle_area(t_a, t_b, t_c)

square_perimeter(s_a)
square_area(s_a)