def a():
    s = list(map(int, list(input())))
    for i in range(10):
        if not i in s:
            return print(i)


def b():
    A, B, K = map(int, input().split())
    cnt = 0
    while K ** cnt < B / A:
        cnt += 1
    print(cnt)

# from math import factorial
# from collections import Counter
# from itertools import permutations
# def c():
#     n, m, k = map(int, input().split())
#     li = [1] * n
#     ans = 0
#     max_ = m
#     for i in range(n):
#
#         for j in range(1, max_ + 1):
#             li[i] = j
#             if sum(li) > k:
#
#             ans += len(list(permutations(li, n)))


    # def recur(sum_, ans_, depth) -> int:
    #     if depth == n:
    #         return k - sum_
    #     for i in range(1, m + 1):
    #         if sum_ + i > k:
    #             break
    #         ans_ = (ans_ + recur(sum_ + i, ans_, depth + 1)) % 998244353
    #     return ans_

    #return print(recur(0, 0, 1))

from bisect import bisect_left, bisect_right
def d():
    n = int(input())
    li = list(map(int, input().split()))
    nums = [[] for _ in range(n + 1)]
    for i, num in enumerate(li):
        nums[num].append(i + 1)
    n = int(input())
    for _ in range(n):
        l, r, x = map(int, input().split())
        if nums[x]:
            print(bisect_right(nums[x], r) - bisect_left(nums[x], l))
        else:
            print(0)

if __name__ == '__main__':
    d()
