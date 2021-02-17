def isPossible(a, n, k):
    dp = [[False for _ in range(k+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1, k+1):
        dp[0][i] = False
    for i in range(1, n+1):
        for j in range(1, k+1):
            if j < a[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]|dp[i-1][j-a[i-1]]
    return dp[n][k]

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t-=1
        n = int(input())
        a = list(map(int, input().strip().split()))
        k = int(input())
        if isPossible(a, n, k):
            print("Yes")
        else:
            print("No")