import re

text = """Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."""

print(re.findall(r"[bB]\S+", text))