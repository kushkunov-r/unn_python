def reverse(in_file, out_file):
    with open(in_file, "r") as input:
        with open(out_file, "w") as output:
            list_lines = input.readlines()
            list_lines.reverse()
            for i in list_lines:
                output.write(i)
        
in_file_name = "lines.txt"
out_file_name = "reverse_" + in_file_name
reverse(in_file_name, out_file_name)