"""
    Given an array, count subsequences having product less than or equal to K.
    [1, 2, 3, 4]; K = 10
    Answer: 11
    The subsets are:
    {1, 2, 3}, {1, 2, 4}, {1}, {2}, {3}, {4}, {1, 2}, {2, 3}, {1, 3}, {2, 4}, {1, 4}

    Let's say I have to find the count of subsets with product <= k and the array given is {a, b, c}.
    If somehow I know the count of subsets (cnt) that satisfy the given condition with
    {a, b} as my array, then for element c, I can always say that the count will at least be
    cnt (ignoring c). 

    For product = floor(k // c), suppose there are x subsets with product
    less than or equal to floor(k // c). I can add c to every such subset and the final
    product of each subset will still remain <= k. Also, just c is an eligible candidate
    for a subset. Therefore dp[i - 1][k // c] + 1 is added to the initial value of cnt 
    if c <= k.

"""

def func(a, k):
    n = len(a)
    dp = [[0 for i in range(k + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j]
            if a[i - 1] <= j and a[i - 1] > 0:
                dp[i][j] += 1 + dp[i - 1][j // a[i - 1]]
    
    return dp[n][k]

if __name__ == '__main__':
    a = list(map(int, input().strip().split()))
    k = int(input())
    print(func(a, k))
