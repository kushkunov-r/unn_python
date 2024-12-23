import ipaddress

def routing(routing_table):
    check = 0
    while check != 1:
        try:
            address = ipaddress.ip_address(input("Введите ip-адрес [192.168.0.100]: "))
            check = 1
        except:
            print("Неверный формат ip-адреса, попробуйте еще раз")
    
    result = ""
    for i in routing_table:
        network = ipaddress.ip_network(routing_table[i][(list(routing_table[i].keys())[0])] +  "/" + routing_table[i]["mask"])
        if address in network:
            result = routing_table[i]["interface"]
    
    if result == "":
        print("Трафик будет удален")
    else:
        print("Трафик будет передан через интерфейс", result)
                         
table_routing = {
                1:{"C": "192.168.1.0", "mask": "255.255.255.0", "interface":"GigabitEthernet0/1"}, 
                2:{"C": "192.168.2.0", "mask": "255.255.255.0", "interface":"GigabitEthernet0/2"}, 
                3:{"C": "192.168.3.0", "mask": "255.255.255.0", "interface":"GigabitEthernet0/3"}, 
                4:{"O": "10.10.1.0", "mask": "255.255.255.0", "interface":"GigabitEthernet0/1"}, 
                5:{"R": "11.0.0.0", "mask": "255.0.0.0", "interface":"GigabitEthernet0/2"}, 
                6:{"D": "173.221.14.0", "mask": "255.255.255.240", "interface":"GigabitEthernet0/3"},
                }

routing(table_routing)
