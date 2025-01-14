def sh_run(config):
    with open(config, "r") as file:
        for line in file:
            if not line.startswith("!"):
                print(line.strip())
            
if __name__ == "__main__":
    config_filename = "config_sw1.txt"
    sh_run(config_filename)