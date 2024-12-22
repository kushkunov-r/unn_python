import ipaddress

def generate_config_ospf(networks, area):
    ospf_net_conf = []
    ospf_template = ["router ospf 1", "router-id 1.1.1.2"]
    ospf_net_conf.extend(ospf_template)
    
    for i in networks:
        wildcard = ipaddress.IPv4Address(int(ipaddress.IPv4Address(networks[i]))^(2**32-1))
        ospf_net_conf.append(i + " " + str(wildcard) + " area " + str(area))       

    return(ospf_net_conf)
    
dict = {
    "10.0.0.0": "255.0.0.0",
    "134.56.0.0": "255.255.0.0",
    "193.193.12.0": "255.255.255.0"
    }

ospf_area = 0
#123

print(generate_config_ospf(dict, ospf_area))