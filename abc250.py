def a():
    s = input()
    print(s * (6 // len(s)))


def b():
    cnt = 0
    n, w = map(int, input().split())
    li = list(map(int, input().split()))
    setli = set()
    for ai in li:
        if ai <= w:
            setli.add(ai)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if li[i] + li[j] <= w:
                setli.add(li[i] + li[j])
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if li[i] + li[j] + li[k] <= w:
                    setli.add(li[i] + li[j] + li[k])
    return print(len(setli))


def c():
    n = int(input())
    dict_li = dict()
    li_key = []
    li_value = []
    set_li = set()
    for i in range(n):
        key, num = input().split()
        if key not in set_li:
            dict_li[key] = i
            li_key.append(key)
            li_value.append(int(num))
            set_li.add(key)
    max_index = li_value.index(max(li_value))
    ans = dict_li[li_key[max_index]] + 1
    print(ans)


def d():
    w = int(input())
    ans = []


def e():
    n = int(input())
    li = list(map(int, input().split()))
    dp = [[0] * (n + 1), [0] * (n + 1)]
    dp[0][0] = li[0]
    dp[1][0] = 10000000
    for i in range(1, n):
        dp[0][i] = min(dp[0][i-1], dp[1][i-1]) + li[i]  # buy
        dp[1][i] = dp[0][i-1]  # dont buy
    ans = min(dp[0][n-1], dp[1][n-1])

    dp = [[0] * (n + 1), [0] * (n + 1)]
    dp[0][0] = 10000000
    dp[1][0] = 0
    for i in range(1, n):
        dp[0][i] = min(dp[0][i - 1], dp[1][i - 1]) + li[i]  # buy
        dp[1][i] = dp[0][i - 1]  # dont buy
    print(min(ans, dp[0][n-1]))


if __name__ == '__main__':
    e()
