from math import sqrt
def a():
    x = int(input())
    return print(sqrt(x*(12800000 + x)))

def b():
    n = int(input())
    return print(n // 10)

def c():
    x1, y1, x2, y2 = map(int, input().split())
    is_lattice = False
    if (abs(x1-x2)==4 or abs(y1-y2)==4) and (abs(x1-x2)==2 or abs(y1-y2)==2):
        is_lattice = True
    elif (abs(x1-x2)==3 or abs(y1-y2)==3) and (abs(x1-x2)==1 or abs(y1-y2)==1):
        is_lattice = True
    elif abs(x1-x2)==3 and abs(y1-y2)==3:
        is_lattice = True
    elif abs(x1-x2)==1 and abs(y1-y2)==1:
        is_lattice = True
    elif (abs(x1-x2)==0 or abs(y1-y2)==0) and (abs(x1-x2)==2 or abs(x1-x2)==4 or abs(y1-y2)==2 or abs(y1-y2)==4):
        is_lattice = True
    if is_lattice:
        return print('Yes')
    else:
        return print('No')

def d():
    A, B, C, D = map(int, input().split())
    pn = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
          103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    # is_takahashi = False
    for i in range(A, B+1):
        li = []
        for j in range(C, D+1):
            k = i + j
            for l in pn:
                if k == l:
                    li.append(j)
                    break
        if not li:
            return print('Takahashi')
    return print('Aoki')

class tree():
    def __init__(self, x):
        self.x = x
        self.next = []

    def next_tree(self):
        for tr_i in self.next:


# WA
def e():
    n, q = map(int, input().split())
    x_li = [tree(0)]
    x_li += [tree(x) for x in list(map(int, input().split()))]
    for i in range(n-1):
        ai, bi = map(int, input().split())
        x_li[ai].next.append(x_li[bi])
    for i in range(q):
        v, k = map(int, input().split())
        li = []
        tmp_tree = x_li[v]
        while tmp_tree.next:






from time import time
if __name__ == '__main__':
    d()
    # print(time() - start)
