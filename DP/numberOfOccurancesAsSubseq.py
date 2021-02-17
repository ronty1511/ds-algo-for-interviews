def func(os, ns, n, m):
    #n is length of originalString and m is length of newString
    if m == 0:
        return 1
    if n == 0:
        return 0
    if os[n-1] == ns[m-1]:
        return (func(os, ns, n-1, m)+func(os, ns, n-1, m-1))
    else:
        return func(os, ns, n-1, m)
        

if __name__ == '__main__':
    for i in range(8):
        originalString = str(input('Enter original string: '))
        newString = str(input('Enter new string: '))
        print(func(originalString, newString, len(originalString), len(newString)))
