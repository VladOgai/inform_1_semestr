mir = ('E', '3', 'J', 'L', 'S', '2', 'Z', '5',
       'A', 'H', 'I', 'M', 'O', 'T', 'U', 'V',
       'W', 'X', 'Y', '1', '8')
mirflag = False
s = input()
i = 0
while i < len(s):
    if s[i] in mir:
        if i == len(s) - 1:
            mirflag = True
        i += 1
    else:
        break
palflag = True if s == s[::-1] else False
if mirflag == True and palflag == True:
    print(s + " is a mirrored palindrome.")
elif mirflag == True and palflag == False:
    print(s + " is a mirrored string.")
elif mirflag == False and palflag == True:
    print(s + " is a regular palindrome.")
elif mirflag == False and palflag == False:
    print(s + " is not a palindrome.")