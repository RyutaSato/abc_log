def a():
    li = list(map(int, input().split()))
    return print(li[li[li[0]]])

def b():
    _ = input()
    ali = list(map(int, input().split()))
    bli = list(map(int, input().split()))
    for i in bli:
        if i in ali:
            ali.remove(i)
        else:
            break
    else:
        return print('Yes')
    return print('No')

def c():
    n = int(input())
    li = [list(input()) for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if i + 6 <= n:
                cnt = 0
                for k in range(6):
                    if li[i + k][j] == '.':
                        cnt += 1
                    if cnt > 2:
                        break
                else:
                    return print('Yes')
            if j + 6 <= n:
                cnt = 0
                for k in range(6):
                    if li[i][j + k] == '.':
                        cnt += 1
                    if cnt > 2:
                        break
                else:
                    return print('Yes')
            if i + 6 <= n and j + 6 <= n:
                cnt = 0
                for k in range(6):
                    if li[i + k][j + k] == '.':
                        cnt += 1
                    if cnt > 2:
                        break
                else:
                    return print('Yes')
            if i - 5 >= 0 and j + 6 <= n:
                cnt = 0
                for k in range(6):
                    if li[i - k][j + k] == '.':
                        cnt += 1
                    if cnt > 2:
                        break
                else:
                    return print('Yes')
    else:
        return print('No')

# TLE
# セグメント木
import numpy as np
def d():
    n = int(input())
    li = np.array([0] * n, dtype='uint64')
    cnt = 0
    for _ in range(n):
        tmp = list(map(int, input().split()))
        # print(f"li:{li}")
        # print(f"tmp:{tmp}")
        if tmp[0] == 1:
            li[cnt] = tmp[1]
            cnt += 1
        if tmp[0] == 2:
            tmpli = li[(li != 0) & (li <= tmp[1])]
            # print(tmpli)
            if len(tmpli) < tmp[2]:
                print(-1)
                continue
            ans = sorted(tmpli.ravel())[-tmp[2]]
            print(ans)
        if tmp[0] == 3:
            tmpli = li[(li != 0) & (li >= tmp[1])]
            # print(tmpli)
            if len(tmpli) < tmp[2]:
                print(-1)
                continue
            ans = sorted(tmpli.ravel())[tmp[2] - 1]
            print(ans)

if __name__ == '__main__':
    d()
