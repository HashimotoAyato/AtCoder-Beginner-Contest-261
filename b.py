n = int(input())
a = [list(input()) for i in range(n)]

check = True
for i in range(n-1):
    for j in range(i+1, n):
        if a[i][j] == 'W' and a[j][i] == 'L':
            continue
        elif a[j][i] == 'W' and a[i][j] == 'L':
            continue
        elif a[i][j] == 'D' and a[j][i] == 'D':
            continue
        else:
            check = False
            break
    if check == False:
        break

if check:
    print('correct')
else:
    print('incorrect')