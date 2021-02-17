"""
    Given n floors and k eggs, find the minimum number of eggs that are to be dropped 
    in worst case to identify the threshold floor. If there are n floors and 1 egg, 
    minimum number of trials required in worst case is n. If there is 1 floor and x eggs
    minimum number of trials required is 1. An egg that breaks cannot be used again.

"""
import sys 

def minTrials(n, k):
    dp = [[0 for i in range(k+1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
        dp[i][1] = i
    for i in range(2, k+1):
        dp[0][i] = 0
        dp[1][i] = 1
    for i in range(2, n+1):
        for j in range(2, k+1):
            minVal = sys.maxsize
            for startingPoint in range(1, i+1):
                minVal = min(minVal, max(dp[i-startingPoint][j], dp[startingPoint-1][j-1]))
            dp[i][j] = 1+minVal
    return dp[n][k]
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input("Enter number of floors:\n"))
        k = int(input("Enter number of eggs:\n"))
        print(minTrials(n, k))