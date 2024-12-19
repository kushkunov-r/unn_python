from module4 import parse_cdp_neighbors

def create_network_map(filenames):
    dict_network_map = {}
    for i in filenames:
        with open(i) as f:
            dict_network_map.update(parse_cdp_neighbors(f.read()))
            
    return(dict_network_map)

if __name__ == "__main__":
    infiles = ["sh_cdp_n_r1.txt", "sh_cdp_n_r2.txt", "sh_cdp_n_r3.txt"] 
    print(create_network_map(infiles))