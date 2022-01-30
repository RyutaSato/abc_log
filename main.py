""" F_236
隣接行列のL乗した後の(i,j)の要素は
    i から j までL回でいく経路の個数
となる
    掛け算 -> and
    足し算 -> or

"""


def f_236():
    n = int(input())
    li = list(map(int, input().split()))



