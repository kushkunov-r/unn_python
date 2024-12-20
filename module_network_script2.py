def convert_ranges_to_ip_list(list):
    ip_list = []
    for i in list:
        if i.count(".") == 3:              
            if not "-" in i.split(".")[-1]:
                ip_list.append(i)
            else:
                start = int(((i.split("-")[0]).split(".")[-1]))
                end = int((i.split("-")[-1]))
                ip = ""
                for iter in range(3):
                    ip = ip + i.split(".")[iter] + "."
                while start <= end:
                    ip_list.append(ip + str(start))
                    start = start + 1
        else:
            so1 = int(((i.split("-")[0]).split(".")[0]))
            so2 = int(((i.split("-")[0]).split(".")[1]))
            so3 = int(((i.split("-")[0]).split(".")[2]))
            so4 = int(((i.split("-")[0]).split(".")[3]))
                       
            eo4 = int(((i.split("-")[1]).split(".")[3]))
                        
            while so4 <= eo4:
                ip_ranges.append(str(so1) + "." + str(so2) + "." + str(so3) + "." + str(so4))
                so4 = so4 + 1               
                
    return(ip_list)
    
ip_ranges = ["8.8.4.4", "1.1.1.1-3", "172.21.41.128-172.21.41.132"]
print(convert_ranges_to_ip_list(ip_ranges))