import re

s = open('2025.txt').readline().strip()
expr = re.findall(r'(?:0|[6-9][06-9]*)(?:[-*](?:0|[6-9][06-9]*))*', s)
expr_len = [len(x) for x in expr]
print(max(expr_len))
