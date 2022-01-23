# AC
def a_236():
    s = input()
    a, b = map(int, input().split())
    return print(f"{s[0:a - 1] + s[b - 1] + s[a:b - 1] + s[a - 1] + s[b:]}")

# AC
def b_236():
    n = int(input())
    cards = list(map(int, input().split()))
    li = [0] * n
    for i in cards:
        li[i - 1] += 1
    return print(li.index(min(li)) + 1)

# AC
def c_236():
    n, m = map(int, input().split())
    local = input().split()
    express = input().split()
    ans = [False] * n
    passed_local = 0
    end_frag = m
    for i in range(m):
        for j in range(passed_local, n):
            if local[j] == express[i]:
                passed_local = j
                ans[j] = True
                break

    for i in ans:
        if i:
            print('Yes')
        else:
            print('No')
    return

# AC
def recur(combi, depth, n, flag, combi_li):
    ans = 0
    if depth == n:
        culc_li = []
        for i in range(len(combi_li)):
            for j in range(i, len(combi)):
                if combi_li[i][0] == combi[j][0] and combi_li[i][1] == combi[j][1]:
                    culc_li.append(combi[j][2])
                    break
        for cul in culc_li:
            ans ^= cul
    else:
        a_i = flag.index(False)
        flag[a_i] = True
        for b_i in range(a_i, len(flag)):
            if not flag[b_i]:
                flag[b_i] = True
                combi_li.append([a_i, b_i])
                ans = max(recur(combi[:], depth + 1, n, flag[:], combi_li[:]), ans)
                combi_li = combi_li[:-1]
                flag[b_i] = False
    return ans


def d_236():
    n = int(input())
    party = []
    for i in range(2*n-1):
        party += list(map(int, input().split()))
    combi = []
    flag = [False] * (2 * n + 1)
    flag[0] = True
    i = 0
    for j in range(1, 2 * n):
        for k in range(j+1, 2 * n + 1):
            combi.append([j, k, party[i]])
            i += 1
    combi_li = []
    return print(recur(combi, 0, n, flag, combi_li))

if __name__ == '__main__':
    d_236()
