"""
Given a list of integers, find the length of longest possible subsequence such that
difference between adjacent elements is 1.
"""

def func(a, n):
    lcs = [1]*n
    for i in range(1, n):
        for j in range(0, i):
            if abs(a[i]-a[j]) == 1 and lcs[j]+1 > lcs[i]:
                lcs[i] = lcs[j]+1
    return max(lcs)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t-=1
        n = int(input())
        a = list(map(int, input().strip().split()))
        print(func(a, n))