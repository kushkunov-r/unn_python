import random

spisok1 = []
spisok2 = []

for i in range(10):
    spisok1.append(random.randint(1, 20))
    spisok2.append(random.randint(1, 20))

print("Первый список:", spisok1)
print("Второй список:", spisok2)

def find_number():
    number = int(input("Введите число которое нужно найти:"))
    if number in spisok1:
        print("В первом списке индексы числа", number, ":")
        for i in range(len(spisok1)):
            if spisok1[i] == number:
                print(i)
    else:
        print("В первом списке числа", number, "нет")
    if number in spisok2:
        print("Во втором списке индексы числа", number, ":")
        for i in range(len(spisok2)):            
            if spisok2[i] == number:
                print(i)
    else:
        print("Во втором списке числа", number, "нет")

def max_count_number():
    big_spisok = []
    numbers_count = {}
    for i in spisok1 + spisok2:
        if i not in big_spisok:
            big_spisok.append(i)
    for i in big_spisok:
        count = 0
        for iter in spisok1 + spisok2:
            if iter == i:
                count = count + 1
        numbers_count.setdefault(i, count)
    max_count = 0
    for i in numbers_count.items():
        if i[1] > max_count:
            max_count = i[1]
    for i in numbers_count.items():
        if i[1] == max_count:
            print("Число", i[0], "встречается чаще всего -", i[1], "раз(а)" )

def multiplication_number(list1, list2):
    factor = int(input("Введите число для умножения каждого элемента обоих списков:"))
    for i in range(len(list1)):
        list1[i] = list1[i] * factor
        list2[i] = list2[i] * factor
    print("Списки после умножения:")
    print("Первый список:", list1)
    print("Второй список:", list2)
    return(list1, list2)

def otrezok():
    list1_match = []
    list2_match = []
    a = int(input("Задайте отрезок: "))
    b = int(input("Задайте отрезок: "))
    if a > b:
        start = b
        end = a
    else:
        start = a
        end = b
    for i in range(len(spisok1)):
        if spisok1[i] >= start and spisok1[i] <= end:
            list1_match.append(spisok1[i])
        if spisok2[i] >= start and spisok2[i] <= end:
            list2_match.append(spisok2[i])
    print("Элементы из первого списка которые попали в отрезок от", start, "до", end, ":", list1_match)
    print("Элементы из первого списка которые попали в отрезок от", start, "до", end, ":", list2_match)

def del_number():
    list1_del = []
    list2_del = []
    number = int(input("Введите число на которое делить элементы:"))
    for i in range(len(spisok1)):
        if spisok1[i] % number == 0 and spisok1[i] not in list1_del:
            list1_del.append(spisok1[i])
        if spisok2[i] % number == 0 and spisok2[i] not in list2_del:
            list2_del.append(spisok2[i])
    print("Элементы из первого списка которые делятся на число", number, "без остатка:", list1_del)
    print("Элементы из первого списка которые делятся на число", number, "без остатка:", list2_del)
    
find_number()
max_count_number()
list1, list2 = multiplication_number(spisok1, spisok2)
otrezok()
del_number()
