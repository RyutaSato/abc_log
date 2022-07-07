def a():
    n = int(input())
    ans = chr(n)

    return print(ans)

def b():
    n, k = map(int, input().split())
    a_li = list(map(int, input().split()))
    b_li = list(map(int, input().split()))
    max_a = max(a_li)
    for i, ai in enumerate(a_li):
        if ai == max_a and i + 1 in b_li:
            return print('Yes')
    return print('No')

def c():
    n = int(input())
    li = []
    for i in range(n):
        li.append(list(map(int, list(input()))))
    ans = []
    for number in range(10):
        idx = []
        for i in li:
            idx.append(i.index(number))
        is_same_li = [0] * 10
        for i in idx:
            is_same_li[i] += 1
        max_same_idx = max(is_same_li)
        if max_same_idx == 1:
            ans.append(max(idx))
        else:
            ans.append((max_same_idx - 1) * 10 + is_same_li.index(max_same_idx))


    return print(min(ans))

from math import comb, factorial
from collections import Counter
def d():
    n = int(input())
    li = list(map(int, input().split()))

    counter = Counter(li)
    ans = comb(n, 3)
    print(ans)
    print(counter.values())
    for i in counter.values():
        if i == 1:
            pass
        else:
            ans -= (n - i) * (n - i - 1)
    return print(ans)


if __name__ == '__main__':
    d()
