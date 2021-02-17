"""
    Given N, find number of ways to make change for N with an infinite supply of
    {c1, c2, ..., cm} coins.
"""
def func(n, m, coins):
    dp = [[1 if j == 0 else 0 for j in range(n+1)] for i in range(m)]
    for i in range(m):
        if i == 0:
            for j in range(1, n+1):
                if j % coins[i] == 0:
                    dp[i][j] = 1
        else:
            for j in range(1, n+1):
                if j < coins[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-coins[i]]
    return dp[m-1][n]


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    coins = list(map(int, input().strip().split()))
    print(func(n, m, coins))