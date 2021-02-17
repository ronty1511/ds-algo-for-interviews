"""
    There are two rows each having n machines (of the same type on both sides).
    Time reqd in each machine is provided (a). Also, time required to switch from
    one row to another at a given point is provided (t). Time to enter and exit each row
    is provided too (e and x respectively). Find the minimum time required for a complete
    operation. One operation is complete when a car passes through each of the n types of
    machines (irrespective of the row). It is given that the car can only move one step
    forward or diagonal (i.e., switch to the next machine on the other row). This problem
    is popularly known as Activity Line Scheduling problem
"""

def computeMinTime(a, t, e, x, n):
    t1 = [0 for i in range(n)]
    t2 = [0 for i in range(n)]
    t1[0] = a[0][0]+e[0]
    t2[0] = a[1][0]+e[1]
    for i in range(1, n):
        t1[i] = min(t1[i-1]+a[0][i], t2[i-1]+a[0][i]+t[1][i])
        t2[i] = min(t2[i-1]+a[1][i], t1[i-1]+a[1][i]+t[0][i])
    return min(t1[n-1]+x[0], t2[n-1]+x[1])

if __name__ == '__main__':
    T = int(input())
    while T > 0:
        T -= 1
        a = []
        t = []
        e = []
        x = []
        n = int(input("Enter number of machines\n"))
        print("Enter first row of A")
        ip = list(map(int, input().strip().split()))
        a.append(ip)
        print("Enter second row of A")
        ip = list(map(int, input().strip().split()))
        a.append(ip)
        print("Enter first row of T")
        ip = list(map(int, input().strip().split()))
        t.append(ip)
        print("Enter second row of T")
        ip = list(map(int, input().strip().split()))
        t.append(ip)
        print("Enter time to enter")
        e = list(map(int, input().strip().split()))
        print("Enter time to exit")
        x = list(map(int, input().strip().split()))
        print(computeMinTime(a, t, e, x, n))