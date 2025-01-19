import csv

def write_dhcp_snooping_to_csv(filenames, output):
    output_list = [["switch", "mac", "ip", "vlan", "interface"]]
    for i in filenames:
        hostname = i.split("_")[0]
        with open(i, "r") as dhcp_snooping:
            for line in dhcp_snooping:
                if ":" in line.split()[0]:
                    output_list.append([hostname, line.split()[0], line.split()[1], line.split()[4], line.split()[5]])
    with open(output, "w") as out:
        writer = csv.writer(out)
        for row in output_list:
            writer.writerow(row)

files = ["sw1_dhcp_snooping.txt", "sw2_dhcp_snooping.txt", "sw3_dhcp_snooping.txt"]
out = "output_snooping.csv"
write_dhcp_snooping_to_csv(files, out)
