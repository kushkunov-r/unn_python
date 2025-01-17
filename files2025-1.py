from pprint import pprint

Sw_all = {"sw0":["Fa0/1", "Fa0/2"], "sw1":["Fa0/1", "Fa0/2"], "sw2":["Fa0/1", "Fa0/2"], "sw3":["Fa0/1", "Fa0/2"], "sw4":["Fa0/1", "Fa0/2"]}                                    

trunk_int = []
mac_endpoint = {}

for i in Sw_all.keys():
    trunk_int.extend(Sw_all[i])

for iter in Sw_all:
    try:
        with open("{}_show mac-address-table.txt".format(iter), "r") as file:
                for line in file:
                    if len(line.strip()) != 0 and line.strip()[0].isdigit():
                        if not line.split()[3] in trunk_int:
                            if not "VLAN" + line.split()[0] in mac_endpoint:
                                mac_endpoint.setdefault("VLAN" + line.split()[0], [line.split()[1]])
                            else:
                                mac_endpoint["VLAN" + line.split()[0]].append(line.split()[1])
    except:
        print("Нет файла конфигурации для {}, добавьте файл конфигурации или удалите {} из словаря".format(iter, iter))

pprint(mac_endpoint)