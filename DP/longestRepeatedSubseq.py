def longestRepeatedSubseq(s, n):
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s[i-1] == s[j-1] and i != j:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][n]

if __name__ == '__main__':
    s = input()
    print(longestRepeatedSubseq(s, len(s)))