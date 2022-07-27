t = int(input())
n = [0]*t
k = [0]*t
for i in range(t):
    n[i],k[i]=input().split()
    n[i] = int(n[i])
    k[i] = int(k[i])
for i in range(t):
    if n[i] < k[i]:
        print('YES')
    else:
        print("NO")
