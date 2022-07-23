l1, r1, l2, r2 = map(int, input().split())

list1 = [False for i in range(101)]
list2 = [False for i in range(101)]

for i in range(l1, r1+1):
    list1[i] = True

for i in range(l2, r2+1):
    list2[i] = True
count = 0
for i in range(101):
    if list1[i] and list2[i]:
        count += 1

if count == 0:
    print(count)
else:
    print(count-1)