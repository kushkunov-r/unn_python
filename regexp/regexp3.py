import re

sentence = """A, very very; irregular_sentence"""  

print(re.sub(r"[,;_]", "", sentence))