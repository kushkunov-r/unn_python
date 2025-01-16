with open("nums.txt", "r") as file:
    summa = 0
    for line in file:
        for i in line.split():
            summa = summa + int(i)
print("Сумма чисел в файле = ", summa)