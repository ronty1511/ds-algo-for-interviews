"""
Given a list of integers, find the maximum subsequence sum such that no three
are consecutive.
"""

def func(a, n):
    dp = [0]*n
    dp[0] = a[0]
    if n == 1:
        return dp[0]
    dp[1] = a[0]+a[1]
    if n == 2:
        return dp[1]
    dp[2] = max(dp[1], a[0]+a[2], a[1]+a[2])
    if n == 3:
        return dp[2]
    for i in range(3, n):
        dp[i] = max(dp[i-1], dp[i-2]+a[i], dp[i-3]+a[i]+a[i-1])
    return dp[n-1]
    

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t-=1
        n = int(input())
        a = list(map(int, input().strip().split()))
        print(func(a, n))