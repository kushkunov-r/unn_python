import re

emails = """zuck26@facebook.com  
page33@google.com  
jeff42@amazon.com"""  

print(re.findall(r"(\S+)[@](\S+)[.](\S+)", emails))