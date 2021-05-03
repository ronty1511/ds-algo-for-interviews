"""
    Given N, find number of ways to make change for N with an infinite supply of
    {c1, c2, ..., cm} coins.
    
    Suppose n = 4 and c = [1, 2, 3], answer = 4. Since there are 4 ways of obtaining 4 using these coins:
    1. {1, 1, 1, 1}
    2. {1, 1, 2}
    3. {1, 3}
    4. {2, 2}
    
    For every element, we can either take at least one in the list or ignore it completely. Let us simulate the above example. Iterating from the end, w can take one 3 
    and look for n = 4 - 3 = 1. Now 3 > 1, we move to 2, and then to 1. Again in the beginning instead of taking the 3, we could've ignored it commpletely and
    moved to 2 straightaway. In that case, we'd be taking one 2, and recur for 4 - 2 = 2. Again we might take the 2 and once we obtain 0, we increment the count
    by 1. Also we might avoid taking the second 2, and shift to 1 instead. This is how the recursion solution works. 
    You can simulate on your own using the following recurrence :
    
    if n == 0:
        return 1
    if n < 0:
        return 0
    if m <= 0 and n >= 1:
        return 0
    return count(c, i - 1, n) + count(c, i, n - c[i - 1])
    
    where c->array of coin denominations, n->size of c
"""

def func(n, m, coins):
    dp = [[1 if j == 0 else 0 for j in range(n+1)] for i in range(m)]
    for i in range(m):
        if i == 0:
            for j in range(1, n+1):
                if j % coins[i] == 0:
                    dp[i][j] = 1
        else:
            for j in range(1, n+1):
                if j < coins[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-coins[i]]
    return dp[m-1][n]


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    coins = list(map(int, input().strip().split()))
    print(func(n, m, coins))
    
    
"""
    Now try to implement it in O(n) space.
"""
