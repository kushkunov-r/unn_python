def sh_run(config):
    ignore = ["duplex", "alias", "configuration"]
    with open(config, "r") as file:
        for line in file:
            if not line.startswith("!"):
                count = 0
                for i in ignore:
                    if i in line:
                        count = count + 1
                if count == 0:
                    print(line.strip())
            
if __name__ == "__main__":
    config_filename = "config_sw1.txt"
    sh_run(config_filename)