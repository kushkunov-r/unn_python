with open("CAM_table.txt", "r") as file:
    list = []
    for line in file:
        if len(line.strip()) != 0 and line.strip()[0].isdigit():
                list.append([int(line.split()[0]), line.split()[1], line.split()[3]])
    
    while True:
        vlan = int(input("Введите номер VLAN [1-4094]: "))
        if vlan >= 1 and vlan <= 4094:
            break
        
    for i in list:
        if vlan == i[0]:
            print("{:6} {:15} {:6}".format(str(i[0]), i[1], i[2]))