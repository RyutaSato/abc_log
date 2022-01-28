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


# TLE
def d_236_tle():
    n = int(input())
    party = []
    for i in range(2 * n - 1):
        party += list(map(int, input().split()))
    combi = []
    flag = [False] * (2 * n + 1)
    flag[0] = True
    i = 0
    for j in range(1, 2 * n):
        for k in range(j + 1, 2 * n + 1):
            combi.append([j, k, party[i]])
            i += 1
    combi_li = []
    return print(recur(combi, 0, n, flag, combi_li))


"""
深さ優先探索で、ペアを作りながら深くしていく、全員ペアが出来た時点で排他的論理和を計算して最大値を出力する
ペアの二人組は左＜右の大きさになるように組む。
再帰関数は、深さ、選んでいる人のフラグ、現時点までの計算結果、現時点での最も高い値
"""


def d_236(n=int(input())):
    party = []
    for i in range(2 * n - 1):
        party += list(map(int, input().split()))
    combi = []
    i = 0
    for j in range(1, 2 * n):
        for k in range(j + 1, 2 * n + 1):
            combi.append([j, k, party[i]])
            i += 1

    # def search_combi(a_i, b_i) -> int:
    #     for pair in combi:
    #         if pair[0] == a_i and pair[1] == b_i:
    #             return pair[2]
    def search_combi(a_i, b_i) -> int:
        return combi[(a_i - 1) * (4 * n - a_i) // 2 + b_i - a_i - 1][2]

    def recur(depth=0, flag=1, ans=0, max_ans=0) -> int:
        if depth == n:
            return ans
        else:
            a_i = 0
            while True:
                if flag & 1 << a_i:
                    a_i += 1
                else:
                    flag |= 1 << a_i
                    break
            for b_i in range(a_i, 2 * n + 1):
                if flag & 1 << b_i:
                    continue
                max_ans = max(max_ans, recur(depth + 1, flag | 1 << b_i, ans ^ search_combi(a_i, b_i), max_ans))
            return max_ans

    ans = recur()
    print(ans)
    return combi


"""
DP,二分探索
ソートされた配列に対してだけでなく、
OKとNGの境目を見つける際に使える
++++++++++++++++++++++++|----------------------------
f(x) = 平均をx以上にできるか
Σa_i >= x * len(list)
Σ(a_i - x) >= 0
dp[i][j]:
    :param
        j:
            0: i番目をとらない
            1: i番目をとる
        ときの最大値

誤差を考慮してlist全体を10^3して計算後、10^-3して出力する。

f(x) = 中央値をx以上にできるか

"""


def e_ave(N, li) -> float:
    dp = [[0, 0] for _ in range(N + 1)]
    pl, pr = min(li), max(li)
    pc = (pr + pl) // 2
    while pr - pl > 5:
        for i in range(1, N + 1):
            dp[i][0] = dp[i - 1][1]
            dp[i][1] = max(dp[i - 1][1] + li[i - 1] - pc, dp[i - 1][0] + li[i - 1] - pc)
        if max(dp[N][0], dp[N][1]) >= 0:
            pl = pc
        else:
            pr = pc
        pc = (pl + pr) // 2
    return pc * (10 ** -4)


def e_med(N, li) -> int:
    dp = [[0, 0] for _ in range(N + 1)]
    pl, pr = min(li), max(li)
    pc = (pr + pl) // 2
    while pr - pl > 5:
        for i in range(1, N + 1):
            if li[i - 1] >= pc:
                dp[i][0] = dp[i - 1][1] + 1
                thred = 1
            else:
                dp[i][0] = dp[i - 1][1]
                thred = -1
            dp[i][1] = max(dp[i - 1][1] + thred, dp[i - 1][0] + thred)
        if max(dp[N][0], dp[N][1]) > 0:
            pl = pc
        else:
            pr = pc
        pc = (pl + pr) // 2
    # print(pl)
    if pl % 10000 == 0:
        return pl // 10000
    else:
        return pl // 10000 + 1


def e_236():
    N = int(input())
    li = list(map(int, input().split()))
    li = [i * 10000 for i in li]
    print(e_ave(N, li))
    print(e_med(N, li))
    return


if __name__ == '__main__':
    d_236()
