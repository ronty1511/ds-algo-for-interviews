"""Given weights and values of N items, put these items in a knapsack of capacity W 
to get maximum total value in each knapsack."""

def func(n, w, vals, wts):
    dp = [[0 for j in range(w+1)] for i in range(n)]
    for i in range(n):
        if i == 0:
            for j in range(1, w+1):
                if j >= wts[i] == 0:
                    dp[i][j] = vals[i]
        else:
            for j in range(1, w+1):
                if j < wts[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-wts[i]]+vals[i])
    return dp[n-1][w]


if __name__ == '__main__':
    n = int(input())
    w = int(input())
    vals = list(map(int, input().strip().split()))
    wts = list(map(int, input().strip().split()))
    print(func(n, w, vals, wts))