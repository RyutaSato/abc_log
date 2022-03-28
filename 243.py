def a():
    v, A, B, C = map(int, input().split())
    v = v % (A+B+C)
    ans = ''
    if v < A:
        ans = 'F'
    elif v < (A + B):
        ans = 'M'
    else:
        ans = 'T'
    return print(ans)

def b():
    n = int(input())
    a_li = list(map(int, input().split()))
    b_li = list(map(int, input().split()))
    cnt_same_all = 0
    cnt_same_num = 0
    for i in range(n):
        if a_li[i] == b_li[i]:
            cnt_same_all += 1
        elif a_li[i] in b_li:
            cnt_same_num += 1
    print(cnt_same_all)
    print(cnt_same_num)

def c():
    n = int(input())
    li = []

    for i in range(n):
        t_x, t_y = map(int, input().split())
        li.append([t_y, t_x])
    s = list(input())
    for i in range(n):
        li[i].append(s[i])
    li.sort()
    tmp_y = li[0][0]
    li_r = []
    li_l = []
    if li[0][2] == 'R':
        li_r.append(li[0][1])
    else:
        li_l.append(li[0][1])
    for i in range(1, n):
        if li[i][0] == tmp_y :
            if li[i][2] == 'R':
                li_r.append(li[i][1])
            else:
                li_l.append(li[i][1])
        else:
            if not li_r or not li_l:
                li_r = []
                li_l = []
                tmp_y = li[i][0]
                continue
            while li_r:
                r = li_r.pop()
                for l in li_l:
                    if r < l:
                        return print('Yes')
            if li[i][2] == 'R':
                li_r = li[i][1]
                li_l = []
            else:
                li_r = []
                li_l = li[i][1]
            tmp_y = li[i][0]
    while li_r:
        r = li_r.pop()
        for l in li_l:
            if r < l:
                return print('Yes')
    return print('No')

"""

if (li[i][1] < tmp_x and li[i][2] == 'R' and tmp_lr == 'L') 
        or (li[i][1] > tmp_x and li[i][2] == 'L' and tmp_lr == 'R'):
    return print('Yes')"""