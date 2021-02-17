import sys

def func(n, cutLengths):
    minval = -sys.maxsize-1
    dp = [minval for i in range(n+1)]
    dp[0] = 0
    for i in range(1, n+1):
        for cut in cutLengths:
            if i-cut >= 0 and dp[i-cut]+1 > dp[i]:
                dp[i] = 1+dp[i-cut]
    return dp[n]

if __name__ == '__main__':
    n = int(input())
    cutLengths = list(map(int, input().strip().split()))
    print(func(n, cutLengths))