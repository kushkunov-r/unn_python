list_vlans = []

with open("sw0_show vlan.txt", "r") as vlans:
    for line in vlans:
        if len(line.strip()) != 0 and line.strip()[0].isdigit() and line.split()[1] == "enet":
            list_vlans.append(int(line.split()[0]))

check = 0
int_vlans = {}

with open("sw0_show interfaces trunk.txt", "r") as int_vlan:
    for line in int_vlan:
        if "Vlans allowed and active" in line:
            check = 1
        elif "Fa" in line and check == 1:
            vlans = line.strip().split()[1].split(",")
            for i in range(len(vlans)):
                vlans[i] = int(vlans[i])
            int_vlans.setdefault(line.strip().split()[0], vlans)
        elif "Vlans in spanning" in line:
            check = 0

list_vlans.sort()

for iter in int_vlans:
    int_vlans[iter] == int_vlans[iter].sort()
    if int_vlans[iter] == list_vlans:
        print("Транковый порт {} - настроен корректно".format(iter))
    else:
        no_vlan = []
        for sw_vlan in list_vlans:
            if not sw_vlan in int_vlans[iter]:
                no_vlan.append(sw_vlan)
        print("Транковый порт {} - настроен не корректно. Отсутствует VLAN {}".format(iter, no_vlan))  