Name = ["Иванов", "Яблочкин","Зайцев","Уткин"]
Book = [["Старик","Море","Один"],["Дом","Крыша","Уехал",],["Луг","Отдых","Пляж"],["Музыка","Кино","Театр"]]
Sales = {"Старик":10,"Море":11,"Один":12,"Дом":10,"Крыша":5,"Уехал":6,"Луг":9,"Отдых":8,"Пляж":10,"Музыка":15,"Кино":14,"Театр":11}
Price = {"Старик":100,"Море":101,"Один":102,"Дом":103,"Крыша":105,"Уехал":106,"Луг":107,"Отдых":108,"Пляж":108,"Музыка":105,"Кино":104,"Театр":105}

def search_author_name():
    while True:
        print("Введите автора: ", Name)
        author = input()
        if author in Name:
            break
        else:
            print("Автор не найден, попробуйте еще раз")
    while True:
        print("Введите название книги: ", Book[Name.index(author)])
        name = input()
        if name in Book[Name.index(author)]:
            break
        else:
            print("Книга не найдена, попробуйте еще раз")
    print("Книга", name, ", стоимостью", Price.get(name), ", продана", Sales.get(name), "раз")
    
def max_price():
    max_cost = []
    for i in Price.items():
        max_cost.append(i[1])
    max_cost = max(max_cost)
    
    for i in Price.items():
        if i[1] == max_cost:
            print("Самая дорогая книга:", i)

def summa_author():
    summa = 0
    while True:
        print("Введите автора: ", Name)
        author = input()
        if author in Name:
            break
        else:
            print("Автор не найден, попробуйте еще раз")
    for i in Book[Name.index(author)]:
        for k in Price:
            if k == i:
                summa = summa + Price[k] * Sales[k]
    print("Общая сумма проданных книг автора", author, "=", summa)
    
def best_author():
    author_summ = {}
    for iter in Name:
        all_book_summa = 0
        for i in Book[Name.index(iter)]:
            summa = 0
            for k in Price:
                if k == i:
                    summa = summa + Price[k] * Sales[k]
                    all_book_summa = all_book_summa + summa
        author_summ.setdefault(iter, all_book_summa)
    author_summ_list = []
    for i in author_summ.items():
        author_summ_list.append(i[1])
    for i in author_summ.items():
        if max(author_summ_list) == i[1]:
            print("Автор с самой большой общей суммой проаднных книг:", i[0], ", Сумма =", i[1])

def all_summ():
    summ = 0
    for i in Sales.items():
        summ = summ + i[1] * Price[i[0]]
    print("Общая сумма продаж всех книг:", summ)

print("1. Поиск книги:")    
search_author_name()
print("\n2. Самая дорогая книга в магазине:")
max_price()
print("\n3. Общая сумма автора:")
summa_author()
print("\n4. Автор у которого самая большая общая сумма:")
best_author()
print("\n5. Общая сумма продаж всех книг:")
all_summ()
