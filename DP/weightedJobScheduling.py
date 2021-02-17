"""
Given start time, end time and profit of a set of jobs, find the maximum profit that 
can be obtained such that no two job timings overlap.

"""

class Job:
    def __init__(self, start, end, profit):
        self.start = start
        self.end = end
        self.profit = profit

def findJobThatDoesntClash(jobList, i):
    j = i - 1
    while j >= 0:
        if jobList[j].end <= jobList[i].start:
            return j
        j -= 1
    return -1

def maxProfit(jobList):
    n = len(jobList)
    dp = [0]*n
    jobList = sorted(jobList, key=lambda x: x.end)
    dp[0] = jobList[0].profit
    for i in range(1, n):
        inc_job = jobList[i].profit
        j = findJobThatDoesntClash(jobList, i)
        if j != -1:
            inc_job += dp[j]
        dp[i] = max(inc_job, dp[i-1])
    return max(dp)

if __name__ == '__main__':
    n = int(input("Enter number of jobs:\n"))
    jobList = []
    for i in range(n):
        start, end, profit = list(map(int, input().strip().split()))
        jobList.append(Job(start, end, profit))
    print(maxProfit(jobList))