def func(a, n, k):
    

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        a = list(map(int, input().strip().split()))
        k = int(input())
        print(func(a, n, k))