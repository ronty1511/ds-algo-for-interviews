"""
Given height of tree, h, determine the number of balanced binary trees possible.
"""

def noOfTrees(n):
    mod = 1000000007
    dp = [0]*(n+5)
    dp[0], dp[1] = 1, 1
    if n == 1:
        return 1
    for i in range(2, n+1):
        dp[i] = (2*dp[i-1]*dp[i-2]%mod+dp[i-1]*dp[i-1]%mod)%mod
    return dp[n]
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t-=1
        n = int(input())
        print(noOfTrees(n))