def a():
    a, b , c, x = map(int, input().split())
    if x <= a:
        return print(1)
    elif a < x <= b:
        return print(c/(b-a))
    else:
        return print(0)

def b():
    s = list(input())
    s.sort()
    return print(''.join(s))

def c():
    n = int(input())
    ans = 0
    li = [0] + [1] * 9 + [0]
    for i in range(n-1):
        tmp_li = [0] * 11
        for j in range(1, 10):
            tmp_li[j] = (li[j] + li[j + 1] + li[j - 1]) % 998244353
        li = tmp_li

    return print(sum(li) % 998244353)

def e():
    q = int(input())
    tmp = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    al = {v: k+1 for k, v in enumerate(tmp)}
    for _ in range(q):
        n = int(input())
        s = list(input())
        cnt_f = 1
        cnt_s = 1
        for i in range(len(s)//2):
            cnt_f *= al[s[i]]
            cnt_s *= al[s[len(s) - i - 1]]
        print(cnt_f % 998244353, cnt_s % 998244353)


if __name__ == '__main__':
    e()