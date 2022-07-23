n = int(input())
s = [input() for i in range(n)]
idx = list(range(n))

z = zip(s, idx)
z = sorted(z)
s, idx = zip(*z)
s = list(s)
idx = list(idx)

add_list = []

count = 0
for i in range(n):
    if i == 0:
        add_list.append('')
    elif s[i] == s[i-1]:
        count += 1
        add_list.append('({})'.format(count))
    else:
        count = 0
        add_list.append('')

for i in range(1,n):
    s[i] = s[i] + add_list[i]

z = zip(idx, s)
z = sorted(z)
idx, s = zip(*z)

for i in range(n):
    print(s[i])
