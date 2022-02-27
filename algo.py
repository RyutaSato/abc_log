from math import sqrt


def code014():
    """
    Factorization
    素因数分解，ユークリッド互除法，最大公約数
    """
    n = int(input())
    li = []
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            li.append(i)
            n //= i
        else:
            i += 1
    li.append(n)
    return print(*li)


def code015():
    """
    Greatest Common Divisor
    素因数分解，ユークリッド互除法，最大公約数
    """
    a, b = map(int, input().split())
    while a >= 1 and b >= 1:
        if a > b:
            a = a % b
        else:
            b = b % a
    if a:
        return print(a)
    else:
        return print(b)


def code016():
    """
    Greatest Common Divisor of N Integers
    素因数分解，ユークリッド互除法，最大公約数
    全ての最大公約数 = ((li[0]とli[1]の最大公約数)とli[2]の最大公約数)の最大公約数．．．
    """
    _ = input()
    li = list(map(int, input().split()))
    while True:
        if 0 in li:
            break
        min_ = min(li)
        li_tmp = [i % min_ for i in li]
        if li_tmp == [0] * len(li_tmp):
            li = li_tmp
            li[0] = min_
            break
        else:
            li = li_tmp
    try:
        min_ = min([i for i in li if i > 0])
    except:
        min_ = 1
    return print(min_)


def code016_retry():
    """
    Greatest Common Divisor of N Integers
    素因数分解，ユークリッド互除法，最大公約数
    全ての最大公約数 = ((li[0]とli[1]の最大公約数)とli[2]の最大公約数)の最大公約数．．．
    """
    _ = input()
    li = list(map(int, input().split()))
    key = li[0]
    for i in li[1:]:
        while i >= 1 and key >= 1:
            if i > key:
                i = i % key
            else:
                key = key % i
        if key == 0:
            key = i
    return print(key)


def code017():
    """
    Least Common Multiple of N Integers
    素因数分解，ユークリッド互除法，最小公倍数
    全ての最小公倍数 = ((li[0]とli[1]の最小公倍数)とli[2]の最小公倍数)の最小公倍数．．．
    """
    _ = input()
    li = list(map(int, input().split()))
    key = li[0]
    for i in li[1:]:
        tmp1, tmp2 = key, i
        while tmp1 >= 1 and tmp2 >= 1:
            if tmp1 > tmp2:
                tmp1 = tmp1 % tmp2
            else:
                tmp2 = tmp2 % tmp1
        if tmp1:
            key = tmp1 * (i // tmp1) * (key // tmp1)
        else:
            key = tmp2 * (i // tmp2) * (key // tmp2)
    return print(key)


def code018():
    """
    組み合わせ，場合の数，丁度和がnとなる場合の数
    """
    _ = input()
    li = list(map(int, input().split()))
    return print(li.count(100) * li.count(400) + li.count(200) * li.count(300))


def code019():
    """
    同じ値を２つ選ぶ場合の数，組み合わせ
    """
    _ = input()
    li = list(map(int, input().split()))
    dic = {i: li.count(i) for i in range(1, 4)}
    cnt = 0
    for k, v in dic.items():
        cnt += v * (v - 1) // 2
    return print(cnt)


def code020():
    """
    n枚からk枚を選んで丁度和がmとなる場合の数，全探索
    そのままではTLE，条件を追加してAC
    """
    n = int(input())
    li = list(map(int, input().split()))
    cnt = 0
    for i in range(0, n - 4):
        for j in range(i + 1, n - 3):
            for k in range(j + 1, n - 2):
                if li[i] + li[j] + li[k] > 1000:
                    continue
                for l in range(k + 1, n - 1):
                    if li[i] + li[j] + li[k] + li[l] > 1000:
                        continue
                    for m in range(l + 1, n):
                        if li[i] + li[j] + li[k] + li[l] + li[m] == 1000:
                            cnt += 1
    return print(cnt)

def code021():
    """
    Combination
    """
    n, r = map(int, input().split())
    ans = 1
    for i in range(n, n-r, -1):
        ans *= i
    for i in range(1, r+1):
        ans //= i
    return print(ans)

def code022():
    """
    和がnとなる２組の数の組み合わせ
    考えられるパターンの枚数で計算
    """
    n = int(input())
    li = list(map(int, input().split()))
    cnt_li = [0] * 100000
    for i in li:
        cnt_li[i] += 1
    ans = 0
    for i in range(1, 50000):
        if cnt_li[i]:
            ans += cnt_li[i] * cnt_li[100000 - i]
    # 50000 and 50000
    ans += cnt_li[50000] * (cnt_li[50000] - 1) // 2
    return print(ans)

def code023():
    n = int(input())
    b_li = list(map(int, input().split()))
    r_li = list(map(int, input().split()))
    ans = (sum(b_li) + sum(r_li)) / n
    return print(ans)

def code024():
    n = int(input())
    ans = 0.0
    for _ in range(n):
        p, q = map(int, input().split())
        ans += q / p
    return print(ans)

def code025():
    n = int(input())
    a_li = list(map(int, input().split()))
    b_li = list(map(int, input().split()))
    ans = 0.0
    for i in range(n):
        ans += (a_li[i] / 3) + (b_li[i] * 2 / 3)
    return print(ans)

def code026():
    """
    n種類を等確率で全種類集めるまでにかかるコストの期待値
    :return:
    """
    n = int(input())
    ans =0.0
    for i in range(1, n + 1):
        ans += n / i
    return print(ans)

def merge_sort(li):
    if len(li) < 4:


def code027():
    """
    Merge Sort
    マージソートアルゴリズム，再帰関数
    :return:
    """
    n = int(input())
    li = list(map(int, input().split()))
    li = merge_sort(li)

if __name__ == '__main__':
    code026()
