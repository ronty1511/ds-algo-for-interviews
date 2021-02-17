def solveTCN2(a, n):
    dp = [[1 for i in range(n)] for i in range(2)]
    res = 0
    for i in range(1, n):
        for j in range(0, i):
            if a[i] > a[j] and dp[0][i] < dp[1][j]+1:
                dp[0][i] = dp[1][j]+1
            if a[i] < a[j] and dp[1][i] < dp[0][j]+1:
                dp[1][i] = dp[0][j]+1
        res = max(res, max(dp[0][i], dp[1][i]))
    return res

def solve(a, n):
    inc, dec = 1, 1
    for i in range(1, n):
        if a[i] > a[i-1]:
            inc = dec + 1
        if a[i] < a[i-1]:
            dec = inc + 1
    return max(inc, dec)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    print(solve(a, n))