class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

def maxChainLen(Parr, n):
    table = []
    for i in range(n):
        table.append([Parr[i].a, Parr[i].b])
    table = sorted(table, key = lambda x: x[1])
    cnt = 1; last = table[0][1]
    for i in range(1, n):
        if table[i][0] > last:
            last = table[i][1]
            cnt += 1
    return cnt

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        tc -= 1
        n = int(input("Enter number of pairs:\n"))
        arr = list(map(int, input().strip().split()))
        Parr = []
        i = 0
        while i < 2*n:
            Parr.append(Pair(arr[i], arr[i+1]))
            i += 2
        print(maxChainLen(Parr, n))
