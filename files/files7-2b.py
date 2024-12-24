def sh_run(input_config, output_config):
    ignore = ["duplex", "alias", "configuration"]
    with open(input_config, "r") as input, open(output_config, "w") as output:
        for line in input:
            if not line.startswith("!"):
                count = 0
                for i in ignore:
                    if i in line:
                        count = count + 1
                if count == 0:
                    output.write(line)
            
if __name__ == "__main__":
    input_config_filename = "config_sw1.txt"
    output_config_filename = "output_" + input_config_filename
    sh_run(input_config_filename, output_config_filename)