with open("CAM_table.txt", "r") as file:
    for line in file:
        if len(line.strip()) != 0 and line.strip()[0].isdigit():
                print("{:6} {:15} {:6}".format(line.split()[0], line.split()[1], line.split()[3]))