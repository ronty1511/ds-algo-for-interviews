"""
    Given n floors and k eggs, find the minimum number of eggs that are to be dropped 
    in worst case to identify the threshold floor. If there are n floors and 1 egg, 
    minimum number of trials required in worst case is n. If there is 1 floor and x eggs
    minimum number of trials required is 1. An egg that breaks cannot be used again.

    If I'm given one egg and I have n floors, I can keep dropping the egg from the topmost
    floor and descend downwards. If at a particular floor it breaks, that'll be my
    threshold floor. Considering the threshold floor to be the ground floor, minimum
    trials in worst case is n. Let us consider I have 5 floors and 2 eggs. I'll pick any
    floor and drop an egg from there. Two outcomes are possible: It breaks or it doesn't.
    
    If it breaks, I'll have to look for the floors below the current floor since the egg will
    break for all the floors above me. Also, I'll have one less egg now since I can't use a
    broken egg.

    If it doesn't break, it won't break for any of the floors below. So I'll have the 
    original number of eggs and I'll have to check for the floors above the current
    floor.
"""

import sys 

def minTrials(n, k): # n: number of eggs, k: number of floors 
    dp = [[0 for i in range(k+1)] for i in range(n+1)]
    for i in range(n + 1):
        dp[i][1] = i
    for i in range(2, k + 1):
        dp[1][i] = 1
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            minVal = sys.maxsize
            for startingPoint in range(1, i + 1):
                minVal = min(minVal, max(dp[i - startingPoint][j], dp[startingPoint - 1][j - 1]))
            dp[i][j] = 1 + minVal
    return dp[n][k]
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input("Enter number of floors:\n"))
        k = int(input("Enter number of eggs:\n"))
        print(minTrials(n, k))
