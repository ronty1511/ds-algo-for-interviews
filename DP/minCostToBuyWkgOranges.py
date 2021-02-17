"""
    cost[i] = cost of i kg of oranges where 1 <= i <= n.
    Find minimum cost to buy W kg of oranges. If impossible, print -1.
    cost[i] = -1 means that i kg packet of orange is unavailable. It may be assumed
    that there is infinite supply of all available packet types.
"""
import sys

def func(cost, n, w):
    dp = [[sys.maxsize for i in range(w+1)] for i in range(n+1)]
    dp[0][0] = 0
    for i in range(1, n+1):
        for j in range(w+1):
            if j == 0:
                dp[i][j] = 0
            elif cost[i-1] != -1:
                if j >= i:
                    minval = min(dp[i-1][j], dp[i][j-i]+cost[i-1])
                    if minval != sys.maxsize:
                        dp[i][j] = minval
                else:
                    dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i][j], dp[i-1][j])
    return dp[n][w] if dp[n][w] != sys.maxsize else -1

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        tc -= 1
        n = int(input())
        cost = list(map(int, input().strip().split()))
        w = int(input())
        print(func(cost, n, w))