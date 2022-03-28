def a():
    _ = int(input())
    s = input()
    return print(s[-1])

def b():
    x, y = 0, 0
    _ = input()
    s = list(input())
    d = 0
    for i in s:
        if i == 'S':
            if d % 4 == 0:
                x += 1
            elif d % 4 == 1:
                y -= 1
            elif d % 4 == 2:
                x -= 1
            else:
                y += 1
        else:
            d += 1
    return print(x, y)

def c():
    n = int(input())
    li = set(range(1, 2 * n + 2))
    while True:
        print(li.pop())
        n = int(input())
        if n == 0:
            break
        li.remove(n)
def d():
    s1, s2, s3 = input().split()
    t1, t2, t3 = input().split()
    is_true = False
    if s1 == t1 and s2 == t2 and s3 == t3:
        is_true = True
    if s1 == t3 and s2 == t1 and s3 == t2:
        is_true = True
    if s1 == t2 and s2 == t3 and s3 == t1:
        is_true = True
    if is_true:
        ans = 'Yes'
    else:
        ans = 'No'
    return print(ans)


def e():
    n, m, len_a, a0, an, even = map(int, input().split())
    g = [[] for _ in range(n+1)]
    ans = [set() for _ in range(len_a+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    print(g)
    dist = [-1] * (n+1)
    ans[0].add(a0)
    ans[len_a].add(an)
    for
    print(dist)



if __name__ == '__main__':
    e()