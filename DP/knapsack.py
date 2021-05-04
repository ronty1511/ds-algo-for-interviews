"""
    Given weights and values of N items, put these items in a knapsack of capacity W 
    to get maximum total value in the knapsack. Each item can be put only once!

    e.g., values = {60, 100, 120} and weights = {10, 20, 30}. The maximum capacity of
    knapsack is 50. I can put (20, 10) or (30, 20) or (10, 30). However to obtain maximum 
    value, I'll put (30, 20) so that I obtain value = 220.

    For every item, I can either pick it (provided its weight is <= the remaining weight
    in the knapsack) or ignore it. The pseudo-code can be given as:

    def recur(vals, weights, max_weight, n):
        if n == 0 or max_weight == 0:
            return 0
        if weights[n - 1] > max_weight:
            return recur(vals, weights, max_weight, n - 1)
        return max(vals[n - 1] + recur(vals, weights, max_weight - weights[n - 1], n - 1),
                   recur(vals, weights, max_weight, n - 1))

    It can be inferred that the problem has optimal substructure property.
    Upon developing the recursion tree, we'll find the same values of n and max_weight
    being calculated over and over again. It would be wiser to store them in a table
    and refer to the value whenever necessary. This is how we're able to detect 
    overlapping subproblem property.

"""

def func(n, w, vals, wts):
    dp = [[0 for j in range(w + 1)] for i in range(n)]
    for i in range(n):
        if i == 0:
            for j in range(1, w + 1):
                if j >= wts[i]:
                    dp[i][j] = vals[i]
        else:
            for j in range(1, w + 1):
                if j < wts[i]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wts[i]] + vals[i])
    return dp[n - 1][w]


if __name__ == '__main__':
    n = int(input())
    w = int(input())
    vals = list(map(int, input().strip().split()))
    wts = list(map(int, input().strip().split()))
    print(func(n, w, vals, wts))
