file = open('input.txt', 'r')
st = file.read()
fl = True
res = 0
for a in st:
    if fl == True and a in ('.', '!', '?'):
        res += 1
        fl = False
    elif a not in ('.', '!', '?'):
        fl = True
print(res)