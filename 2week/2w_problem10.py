f = open('input.txt', 'r')
glas = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
sogl = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
lst = list(str(f.read()).split())
res = []
for sl in lst:
    i = 1
    while i < len(sl):
        if sl[i] in glas and sl[i-1] in sogl:
            sl = sl[:i + 1] + 'c' + sl[i].lower() + sl[i + 1:]
            i += 2
        elif sl[i] in glas and sl[i - 1] in ('ь', 'ъ'):
            if sl[i] in ('а', 'я'):
                sl = sl[:i + 1] + 'cа' + sl[i + 1:]
                i += 2
            elif sl[i] == 'ю':
                sl = sl[:i + 1] + 'cу' + sl[i + 1:]
                i += 2
        else:
            i += 1
    res.append(sl)
print(*res)