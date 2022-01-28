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
    dp = [[0, 0] for _ in range(N+1)]
    pl, pr = min(li), max(li)
    pc = (pr + pl) // 2
    while pr - pl > 5:
        for i in range(1, N + 1):
            dp[i][0] = dp[i-1][1]
            dp[i][1] = max(dp[i-1][1] + li[i-1] - pc, dp[i-1][0] + li[i-1] - pc)
        if max(dp[N][0], dp[N][1]) >= 0:
            pl = pc
        else:
            pr = pc
        pc = (pl + pr) // 2
    return pc * (10 ** -4)


def e_med(N, li) -> int:
    dp = [[0, 0] for _ in range(N+1)]
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
    #print(pl)
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
    e_236()
