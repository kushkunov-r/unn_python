int_vlan = {}

with open("sw0_show running-config.txt", "r") as run_conf:
    for line in run_conf:
        if "FastEthernet" in line:
            interface = "Fa" + line[22:].strip()
        elif "switchport access vlan" in line:
            int_vlan.setdefault(interface, int(line[24:]))
            
with open("sw0_show mac-address-table_without_vlan.txt", "r") as mac_table:               
    for line in mac_table:
        if len(line.strip()) != 0 and line.strip()[0].isdigit():
            for i in int_vlan:
                if line.split()[2] == i:
                    print("Устройство {} подключено к VLAN {}".format(line.split()[0], int_vlan[i]))