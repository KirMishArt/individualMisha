import re

text = "Hello World! HOW are you? I'M FINE."
pattern = r'\b[A-Z]+\b'

matches = re.findall(pattern, text)
print(matches)
