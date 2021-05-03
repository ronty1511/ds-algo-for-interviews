"""
Given two strings, find the minimum number of operations required to convert
one string to another. Valid operations can be given as:
1. Insert
2. Delete
3. Replace

e.g., "sunday"->"saturday" requires insertion of 'a' and 't' and replacement of 'n' and 'r'.
So it requires at least 3 operations. 

A simple intuition can be obtained from the above example.
If the last characters in both the string are same, we don't need to bother about it
and we can confidently deal with the rest of the strings. This is why recursion comes
into play. In this case, 'day' is present AT THE END OF BOTH THE STRINGS. So we need
to care only about "sun" and "satur". Now the last letters are different. Here we'll
let recursion find out the cost of replacing the letters or deleting from any of the
two strings. The one with minimum cost will be returned. That is, we'll calculate 
cost of changing "sun" to "satu" (insertion), cost of changing "su" to "satur" (deletion)
and cost of changing "su" to "satu" (replacement).
It is very important to figure out if the recursion tree has optimal substructure
and overlapping subproblems for it to be eligible for dp. As we see ("su", "satu")
appears in case of replacement and again in case of deletion after following
insertion in the above explanation, we need to employ memoization to store the result.
"""

def func(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
    for i in range(1, len1 + 1):
        dp[i][0] = i
    for i in range(1, len2 + 1):
        dp[0][i] = i
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] != str2[j - 1]:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
            else:
                dp[i][j] = dp[i - 1][j - 1]
    return dp[len1][len2]

if __name__ == '__main__':
    str1 = input('Enter first string\n')
    str2 = input('Enter second string\n')
    print(func(str1, str2))
