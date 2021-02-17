import sys

def func(ar, n):
    dp = [[0 for i in range(n)] for i in range(n)]
    for L in range(2, n+1):
        for i in range(1, n-L+1):
            j = i+L-1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                val = dp[i][k]+dp[k+1][j]+ar[i-1]*ar[k]*ar[j]
                if val < dp[i][j]:
                    dp[i][j] = val
    return dp[1][n-1]

if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().strip().split()))
    print(func(ar, n))