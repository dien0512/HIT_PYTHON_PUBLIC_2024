next_char = lambda a, b: chr(ord(a) + 1) if ord(a) < ord(b) else a
print(next_char('z','a'))
print(next_char('b','b'))