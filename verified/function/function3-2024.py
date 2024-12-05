import random

VLANs = []

def create_spisok_vlans():
    spisok = []
    len_spisok = int(input("Введите длину списка: "))
    count = 0
    while count != len_spisok:
        vlan_add = random.randint(1, 4094)
        if vlan_add not in spisok:
            spisok.append(vlan_add)
            count = count + 1
    spisok.sort()
    print("Список VLAN-ов: ", spisok)
    return(spisok)

def delete_vlan(spisok):
    print("Исходный список VLAN-ов", spisok)
    while True:
        del_vlan = int(input("Введите VLAN который нужно удалить:"))
        if del_vlan in spisok:
            break
        print("Такого VLAN-а нет в списке, попробуйте еще раз")
    spisok.remove(del_vlan)
    print("Список после удаления: ", spisok)
    return(spisok)

def find_vlan(spisok):
    print("Исходный список VLAN-ов", spisok)
    vlan = int(input("Введите VLAN который нужно найти: "))
    if vlan in spisok:
        print("Введенный VLAN есть в списке")
    else:
        print("Введенного VLAN-а нет в списке")
        
def add_vlan(spisok):
    print("Исходный список VLAN-ов", spisok)
    while True:
        vlan = int(input("Введите VLAN который нужно добавить [1 - 4094]:"))
        if vlan > 0 and vlan < 4095:
            break
        else:
            print("VLAN введен не корректно, попробуйте еще раз")
    if vlan not in spisok:
        spisok.append(vlan)
        spisok.sort()
        print("Cписок VLAN-ов после добавления:", spisok)
    else:
        print("Такой VLAN уже есть в списке")
    return(spisok)

def vers_list(spisok1):
    print("Исходный список VLAN-ов", spisok1)
    spisok2 = []
    counter = 0
    len_spisok2 = int(input("Введите длину второго списка VLAN-ов:"))
    while counter != len_spisok2:
        vlan = int(input("Заполните список не повторяющимися VLAN-ами:"))
        if vlan not in spisok2:
            spisok2.append(vlan)
            counter = counter + 1
        else:
            print("Такой VLAN уже есть в списке, попробуйте еще раз")
    spisok2.sort()
    print("Второй список VLAN-ов", spisok2)
    if len(spisok1) == len(spisok2):
        len_spiskov = len(spisok1)
        count = 0
        for i in range(len_spiskov):
            if spisok1[i] == spisok2[i]:
                count = count + 1
        if count == len_spiskov:
            print("Списки равной длины и равны по элементно")
        else:
            print("Списки равной длины, но не равны по элементно")
    else:
        print("Списки разной длинны, а значит не равны")
            
def clear_vlans(spisok):
    spisok.clear()
    print("Все VLAN-ы в списке удалены")
    return(spisok)
    
def add_spisok_vlans(spisok1):
    print("Исходный список VLAN-ов", spisok1)
    spisok2 = []
    counter = 0
    len_spisok2 = int(input("Введите длину второго списка VLAN-ов:"))
    while counter != len_spisok2:
        vlan = int(input("Заполните список не повторяющимися VLAN-ами:"))
        if vlan not in spisok2:
            spisok2.append(vlan)
            counter = counter + 1
        else:
            print("Такой VLAN уже есть в списке, попробуйте еще раз")
    for i in spisok2:
        spisok1.append(i)
    spisok1.sort()
    print("В первый список VLAN-ов добавлен второй:", spisok1)
    return(spisok1)

print("1. Создаем список заданной длинны, заполняем случайными числами и упорядочиваем его")
VLANs = create_spisok_vlans()
print("\n2. Удаляем введенный VLAN в списке с проверкой корректного ввода VLAN-а и наличия его в списке")
VLANs = delete_vlan(VLANs)
print("\n3. Ищем введенный VLAN в списке")
find_vlan(VLANs)        
print("\n4. Добавляем введенный VLAN в список с проверкой на дубли и упорядочиваем его")
VLANs = add_vlan(VLANs)
print("\n5. Вводим второй список с клавиатуры с проверкой корректности ввода, упорядочиваем и сравниваем с первым списком (длина и элементы)")
vers_list(VLANs)
print("\n6. Очищаем список вланов")
VLANs = clear_vlans(VLANs)
print("\n7. Добавляем введенный с клавиатуры список VLAN-ов в первый список")
VLANs = add_spisok_vlans(VLANs)

    
