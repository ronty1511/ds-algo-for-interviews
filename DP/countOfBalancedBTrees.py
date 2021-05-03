"""
Given height of tree, h, determine the number of balanced binary trees possible.
"""

def noOfTrees(n):
    mod = 1000000007
    dp = [0]*(n + 5)
    dp[0], dp[1] = 1, 1
    if n == 1:
        return 1
    for i in range(2, n + 1):
        dp[i] = (2 * dp[i-1] * dp[i-2] % mod + dp[i-1] ** 2 % mod) % mod
    return dp[n]
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t-=1
        n = int(input())
        print(noOfTrees(n))
        
"""
    Idea: For balanced B-trees, difference of heights of left and right subtrees can be
    atmost 1. So for height h, the possible heights for left and right subtrees can be:
    
             LEFT  | RIGHT
            --------------
             h - 1 | h - 2
            --------------
             h - 2 | h - 1
            --------------
             h - 1 | h - 1
             
   This is beacuse height of a tree = 1 + max(height of left subtree, height of right subtree). 
   Now for height h, one of the subtrees has to have height = h - 1. Since the tree is balanced,
   height of the other subtree is at least h - 2.
   
   Therefore, dp[h] = dp[h - 1] * dp[h - 2] + dp[h - 2] * dp[h - 1] + dp[h - 1] * dp[h - 1].
"""
