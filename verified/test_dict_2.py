Dict_interface={"FastEthernet0/1":{"mode":"switchport mode access","vlan":10},
                "FastEthernet0/2":{"mode":"switchport mode access","vlan":11},
                "FastEthernet0/3":{"mode":"switchport mode access","vlan":12},
                "GigabitEthernet0/1":{"mode":"switchport mode trunk","switchport trunk allowed vlan":[10,11,12]},
                "GigabitEthernet0/2":{"mode":"switchport mode trunk","switchport trunk allowed vlan":[10,15,26]}}

List_vlan=[1,10,12,15]

for i in Dict_interface:
    if "access" in Dict_interface[i]["mode"] and not Dict_interface[i]["vlan"] in List_vlan:
        Dict_interface[i]["vlan"] = 1
    elif "trunk" in Dict_interface[i]["mode"]:
            for iter in Dict_interface[i]["switchport trunk allowed vlan"]:
                if not iter in List_vlan:
                    Dict_interface[i]["switchport trunk allowed vlan"].remove(iter)
                    
print(Dict_interface)
