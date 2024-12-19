import mod1
import mod2

one = int(input("Введите первое число"))
two = int(input("Введите второе число"))

print("\nВведенные числа четные или нет:")
mod1.chetn(one, two)
print("\nПоиск максимального числа из двух чисел:")
mod1.max(one, two)
print("\nКакое число делится на 5:")
mod1.del5(one, two)
print("\nНахождение суммы двух чисел:")
mod2.sum(one, two)
print("\nПодсчет квадрата для каждого числа:")
mod2.kvadr(one, two)
