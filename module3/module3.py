from figures.triangle.code import *
from figures.square.code import *


t_a = input("Введите первую сторону треугольника: ")
t_b = input("Введите вторую сторону треугольника: ")
t_c = input("Введите третью сторону треугольника: ")
  
s_a = input("Введите сторону квадрата: ")

if t_a and t_b and t_c:
    triangle_perimeter(int(t_a), int(t_b), int(t_c))
    triangle_area(int(t_a), int(t_b), int(t_c))
else:
    triangle_perimeter()
    triangle_area()

if s_a:
    square_perimeter(int(s_a))
    square_area(int(s_a))
else:
    square_perimeter()
    square_area()