def parse_cdp_neighbors(a):
    dict_connect = {}
    my_hostname = ""
    
    for i in a:
        if i == "#":
            break
        else:
            my_hostname = my_hostname + str(i)
    
    a = a.split()
    
    for i in range(len(a)):
        if a[i] == "Port" and a[i+1] == "ID":
            start = i + 2
        if a[i] == "Total":
            end = i
            
    while start < end:
        dict_connect.setdefault((my_hostname, (a[start+1] + a[start+2])), ((a[start], a[start+8] + a[start+9])))
        start = start + 10
    
    return(dict_connect)

if __name__ == "__main__":
    with open("sh_cdp_n_r1.txt") as f:
        print(parse_cdp_neighbors(f.read()))