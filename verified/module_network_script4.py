import ipaddress

def neighbor_interface(interface, neighbors):
    for i in interface:
        for iter in neighbors:
            if (interface[i]["IP-address"]).split(".")[0:3] == (neighbors[iter]["IP-address"]).split(".")[0:3]:
                print(iter, "подключен через интерфейс", i)

Dict_interface = {
                "GigabitEthernet0/0": {"IP-address":"192.168.1.1", "OK":"YES", "Method":"manual", "Status":"Up", "Protocol":"Up"},
                "GigabitEthernet0/1": {"IP-address":"192.168.2.1", "OK":"YES", "Method":"manual", "Status":"Up", "Protocol":"Up"},
                "GigabitEthernet0/2": {"IP-address":"unassigned", "OK":"YES", "Method":"manual", "Status":"Down", "Protocol":"Down"},
                "Serial0/3/0": {"IP-address":"192.168.23.1", "OK":"YES", "Method":"manual", "Status":"Up", "Protocol":"Up"},
                "Serial0/3/1": {"IP-address": "11.12.12.2", "OK":"YES", "Method":"manual", "Status":"Down", "Protocol":"Down"}
                }
                
dict_cdp_neighbors = {
                    "Switch1":{"IP-address":"192.168.1.2"},
                    "Switch2":{"IP-address":"192.168.2.3"},
                    "Router_4":{"IP-address":"192.168.23.2"},
                    "Router_3":{"IP-address":"11.12.12.3"}
                    }

neighbor_interface(Dict_interface, dict_cdp_neighbors)
