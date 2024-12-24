with open("CAM_table.txt", "r") as file:
    list = []
    for line in file:
        if len(line.strip()) != 0 and line.strip()[0].isdigit():
                list.append([int(line.split()[0]), line.split()[1], line.split()[3]])
                
    for i in sorted(list):
        print("{:6} {:15} {:6}".format(str(i[0]), i[1], i[2]))