"""
    Given an array of integers, find the length of longest alternating subsequence.
    e.g., A = {10, 22, 9, 33, 49, 50, 31, 60}; answer = 6. 
    One of the many solution subsequences can be {10, 22, 9, 33, 31, 60}.

    If I maintain two arrays, each with size n, where ith element of first array 
    stores count of longest alternating subsequence with A[i] < the previous element
    and ith element of second array stores count of longest alternating subsequence
    with A[i] > previous element, I can get those values for calculating the subsequent
    cells.

    For first i values, dp[0][i] = max(dp[0][i], 1 + dp[1][j]) where j < i and
                        dp[1][i] = max(dp[1][i], 1 + dp[0][j]) where j < i.

    This takes O(n^2) time. There's a better solution.

    Upon close observation, it can be inferred that for a particular i, we need 
    to store the maximum counts for (i-1)th element greater than the previous element 
    and less than the previous element (in the longest subsequences) only. If our current
    element is less than the previous element, inc = dec + 1. If it is greater than
    the previous value, dec = inc + 1. This is because at any i, inc and dec represent
    the length of longest alternating subsequences with a[i] greater than the previous
    element in the subsequence and the length of subsequence with a[i] less than the 
    previous element in subsequence respectively.

    inc (at ith iteration) = max. length of subsequence ending with a[i] greater than
    previous element.
    dec (at ith iteration) = max. length of subsequence ending with a[i] less than
    previous element.
    
    Time complexity is reduced to O(n) and space complexity is reduced to O(1).
    
"""

def solveTCN2(a, n):
    dp = [[1 for i in range(n)] for i in range(2)]
    res = 0
    for i in range(1, n):
        for j in range(0, i):
            if a[i] > a[j] and dp[0][i] < dp[1][j] + 1:
                dp[0][i] = dp[1][j] + 1
            if a[i] < a[j] and dp[1][i] < dp[0][j] + 1:
                dp[1][i] = dp[0][j] + 1
        res = max(res, max(dp[0][i], dp[1][i]))
    return res

def solve(a, n):
    inc, dec = 1, 1
    for i in range(1, n):
        if a[i] > a[i - 1]:
            inc = dec + 1
        if a[i] < a[i - 1]:
            dec = inc + 1
    return max(inc, dec)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    print(solve(a, n))
