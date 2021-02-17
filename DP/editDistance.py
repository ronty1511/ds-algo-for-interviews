"""Given two strings, find the minimum number of operations required to convert
one string to another. Valid operations can be given as:
1. Insert
2. Delete
3. Replace"""

def func(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
    for i in range(1, len1+1):
        dp[i][0] = i
    for i in range(1, len2+1):
        dp[0][i] = i
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if str1[i-1] != str2[j-1]:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
            else:
                dp[i][j] = dp[i-1][j-1]
    return dp[len1][len2]

if __name__ == '__main__':
    str1 = input('Enter first string\n')
    str2 = input('Enter second string\n')
    print(func(str1, str2))