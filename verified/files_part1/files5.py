with open ("ospf.txt", "r") as file:
    for line in file:
        print("{:20} {:20}".format("Prefix", line.split()[1]))
        print("{:20} {:20}".format("AD/Metric", line.split()[2].strip("[]")))
        print("{:20} {:20}".format("Next-Hop", line.split()[4].strip(",")))
        print("{:20} {:20}".format("Last update", line.split()[5].strip(",")))
        print("{:20} {:20}".format("Outbound Interface", line.split()[6]))
        print("")