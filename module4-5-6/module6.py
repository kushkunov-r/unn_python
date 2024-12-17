from draw_network_graph import draw_topology
from module5 import create_network_map

def unique_network_map(topology_dict):
    unique_dict = {}
    
    for i in topology_dict:
        if not topology_dict[i] in unique_dict:
            unique_dict.setdefault(i, topology_dict[i])          
    
    return unique_dict
    

if __name__ == "__main__":
    infiles = ["sh_cdp_n_r1.txt", "sh_cdp_n_r2.txt", "sh_cdp_n_r3.txt"] 
    draw_topology(unique_network_map(create_network_map(infiles)))
    unique_network_map(create_network_map(infiles))
    