n = int(input())

C = [[0 for x in range(n+1)] for x in range(n+1)]

for i in range(n+1):
    for j in range(min(i, n)+1):
        if j == 0 or j == i:
            C[i][j] = 1
        else:
            C[i][j] = C[i-1][j-1] + C[i-1][j]

q = int(input())
while q > 0:
    q -= 1
    x = int(input())
    if x > n:
        print("INVALID")
        break
    print(C[n][x])