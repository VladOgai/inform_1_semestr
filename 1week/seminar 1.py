

# упражнение 1


a, b = tuple(map(int, input().split()))
print(a + b)
print(a - b)
print(a * b)


# упражнение 2


a = str(input())
print(a[-1])


# упражнение 3


summ = list(map(int, input().split()))
s = 1
for n in summ:
    s *= n
print(round(s ** (1/len(summ)), 8))


# упражнение 4


fil = open('input4.txt')
out = open('output4.txt', 'w')
lst = []
for line in fil:
    lst.append(line)
nums = list(map(float, lst[0].split()))
match lst[1]:
    case '+':
        out.write(str(round(sum(nums), 6)))
    case '-':
        s = 0
        for n in nums:
            if n == nums[0]:
                s += n
            else:
                s -= n
        out.write(str(round(s, 6)))
    case '*':
        s = 1
        for n in nums:
            s *= n
        out.write(str(round(s, 6)))


# упражнение 5


N = list(input())
N.reverse()
b = int(input())
c = int(input())
n10 = 0
for i in range(len(N)):
    n10 += (int(N[i]) * (b ** i))
nc = []
while True:
    a = n10 // c
    bb = n10 % c
    nc.append(bb)
    if a == 0:
        break
    n10 = a
nc.reverse()
print(''.join(map(str, nc)))


# упражнение 6


fil = open('input6.txt')
out = open('output6.txt', 'w')
lst = []
for line in fil:
    lst.append(line)
nums = list(map(int, lst[0].split()))
b = int(lst[2])
for j in range(len(nums)):
    n10 = 0
    for i in range(len(str(nums[j]))):
        n10 += (int(str(nums[j])[i]) * (b ** i))
    nums[j] = n10
res = 0
lst[1].strip()
match lst[1]:
    case '+\n':
        res = round(sum(nums), 6)
    case '-\n':
        s = 0
        for n in nums:
            if n == nums[0]:
                s += n
            else:
                s -= n
        res = round(s, 6)
    case '*\n':
        s = 1
        for n in nums:
            s *= n
        res = round(s, 6)
nc = []
while True:
    a = res // b
    oss = res % b
    nc.append(oss)
    if a == 0:
        break
    res = a
nc.reverse()
out.write(''.join(map(str, nc)))