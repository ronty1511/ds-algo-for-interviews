def maxSum(arr):
    n = len(arr)
    dp = [arr[i] for i in range(n)]
    for i in range(1, n):
        maxval = 0
        for j in range(0, i):
            if arr[j] < arr[i] and dp[j] > maxval:
                maxval = dp[j]
        dp[i] += maxval
    return max(dp)

if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    print(maxSum(arr))