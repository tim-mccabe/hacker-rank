if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a = list(arr)
    m = max(a)
    l = []
    for i in a:
        if i != m:
            l.append(i)
    print(max(l))