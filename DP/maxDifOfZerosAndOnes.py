"""
    Given a string of 0's and 1's, return the largest difference between count of 0's
    and count of 1's in any subarray. Kadane's algorithm has been employed here but
    it can be done in a different way that takes O(n) space.
"""

def func(S):
    current_sum = 0
    max_sum = 0
    size = len(S)
    flag = False
    for i in range(size):
        if S[i] == '0':
            flag = True
            break
    if flag == False:
        return -1
    for i in range(0, size):
        current_sum += 1 if S[i] == '0' else -1
        if current_sum < 0:
            current_sum = 0
        max_sum = max(max_sum, current_sum)
    return max_sum
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        print(func(s))