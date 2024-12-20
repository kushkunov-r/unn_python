import subprocess

def ping_ip_addresses(list_ip_add):
    access_list = []
    inaccess_list = []
    for i in list_ip_add:
        result = subprocess.run(["ping", "-c", "1", i], stdout=subprocess.DEVNULL)
        if result.returncode == 0:
            access_list.append(i)
        else:
            inaccess_list.append(i)
    return(access_list, inaccess_list)
        
list = ["192.168.1.1", "8.8.8.8", "1.1.1.1"]
print(ping_ip_addresses(list))