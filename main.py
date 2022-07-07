def a():
    return print("{:02}".format((int(input())) % 100))

def b():
    n = int(input())
    print(1)
    li = [1, 1]
    if n > 1:
        print(*li)

    for _ in range(n-2):
        len_li = int(len(li)) - 1
        new_li = []
        new_li.append(1)
        for i in range(len_li):
            new_li.append(li[i] + li[i+1])
        new_li.append(1)
        li = new_li
        print(*li)

def c():
    n, k = map(int, input().split())
    li = list(map(int, input().split()))
    tmp_li = []
    for i in range(k):
        li_li = li[i::k]
        li_li.sort()
        tmp_li.append(li_li.copy())
    new_li = []
    for i in range(k):
        for j in tmp_li:
            if len(j) <= i:
                continue
            new_li.append(j[i])
    print(new_li)
    i = 1
    while i < n:
        if new_li[i-1] <= new_li[i]:
            i += 1
        else:
            return print('No')
    return print('Yes')

from bisect import bisect
def prime_(n, max_n):
    cnt = 0
    for i in range(1, n//2 + 1):
        if i * i > n:
            break
        if n % i == 0:
            j = n // i
            if max_n >= j:
                if i == j:
                    cnt += 1
                else:
                    cnt += 2
    return cnt

def d():
    n = int(input())
    ans = 1
    for i in range(2, n+1):
        ans += prime_(i*i, n)
        # print(f"ans:{ans} i:{i}")
    return print(ans)


if __name__ == '__main__':
    c()
