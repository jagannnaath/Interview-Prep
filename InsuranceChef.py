t = int(input())
x = [0]*t
y = [0]*t
for i in range(t):
    x[i],y[i] = input().split()
    x[i] = int(x[i])
    y[i] = int(y[i])
for i in range(t):
    if x[i] >= y[i]:
        print(y[i])
    else:
        print(x[i])
