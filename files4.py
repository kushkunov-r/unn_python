def summa(file):
    with open(file, "r") as text:
        summa = 0
        for i in text.readlines():
            summa = summa + int(i.split()[1]) * int(i.split()[2])
        return(summa)
        
file_name = "prices.txt"
print(summa(file_name))