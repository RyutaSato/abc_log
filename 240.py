def a():
    a, b = map(int, input().split())
    if b-a == 1 or (b==10 and a==1):
        return print('Yes')
    else:
        return print('No')

def b():
    n = int(input())
    li = set(list(map(int, input().split())))
    return print(len(li))

def c():
    n, x = map(int, input().split())
    li = {0}
    for i in range(n):
        ai, bi = map(int, input().split())
        tmp_li = []
        for j in li:
            tmp_li.append(j+ai)
            tmp_li.append(j+bi)
        li = set(tmp_li)
    if x in li:
        return print('Yes')
    else:
        return print('No')

# RE
from collections import deque
def d():
    n = int(input())
    li = list(map(int, input().split()))
    ans = deque()
    for i in range(n):
        if ans and ans[-1] == li[i]:
            is_true = True
            for j in range(1, li[i]):
                if ans[-j] != li[i]:
                    is_true = False
                    break
            if is_true:
                for j in range(li[i] - 1):
                    ans.pop()
            else:
                ans.append(li[i])
        else:
            ans.append(li[i])
        print(len(ans))



from time import time
if __name__ == '__main__':
    d()
    # print(time() - start)
