import re

tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today https://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''  

print(re.sub(r"\b\W*\b", "", tweet))