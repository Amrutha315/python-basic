n = input()
i = 0
while i < len(n):
    if 'A' <= n[i] <=  'Z':
        str += chr(ord(n[i]) + 32)
    else:
        str += n[i]
    i += 1
print(str)