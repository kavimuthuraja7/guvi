import re
pattern = r"[A-Z]"
text = "a"

if re.match(pattern, text):
    print('ok')
else:
    print('not ok')
