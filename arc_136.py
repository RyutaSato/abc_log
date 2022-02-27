def a_arc136():
    n = int(input())
    s = list(input())
    for i in range(n):
        if s[i] == 'A':
            s[i] = 'BB'
    s = list(''.join(s))
    ans = []
    i = 0
    while i < len(s) - 1:
        if s[i] == 'C':
            ans.append('C')
        elif s[i] == 'B' and s[i + 1] == 'B':
            ans.append('A')
            i += 1
        else:
            ans.append('B')
        i += 1

    if i < len(s) and s[i] == 'C':
        ans.append('C')
    elif i < len(s) and s[i] == 'B':
        ans.append('B')
    return print(''.join(ans))


# WA 5case
def b_arc136():
    n = int(input())
    a_li = list(map(int, input().split()))
    b_li = list(map(int, input().split()))

    check_a = [0] * 5001
    check_b = [0] * 5001
    for i in range(n):
        check_a[a_li[i]] += 1
        check_b[b_li[i]] += 1
    if check_a != check_b:
        return print('No')
    i = 0
    while i < n - 2:
        if a_li[i] == b_li[i]:
            i += 1
        else:
            ai = a_li[i:].index(b_li[i]) + i
            while ai - i > 1:
                a_li[ai - 2], a_li[ai - 1], a_li[ai] = a_li[ai], a_li[ai - 2], a_li[ai - 1]
                ai -= 2
            if ai - i == 0:
                i += 1
            elif ai - i == 1:
                a_li[ai - 1], a_li[ai], a_li[ai + 1] = a_li[ai], a_li[ai + 1], a_li[ai - 1]
                i += 1
    #
    # print(f"a_li: {a_li}")
    # print(f"b_li: {b_li}")
    flag = False
    if a_li[n-1] == b_li[n-1] and a_li[n-2] == b_li[n-2] and a_li[n-3] == b_li[n-3]:
        flag = True
    a_li[n - 3], a_li[n - 2], a_li[n - 1] = a_li[n - 1], a_li[n - 3], a_li[n - 2]
    if a_li[n - 1] == b_li[n - 1] and a_li[n - 2] == b_li[n - 2] and a_li[n - 3] == b_li[n - 3]:
        flag = True
    a_li[n - 3], a_li[n - 2], a_li[n - 1] = a_li[n - 1], a_li[n - 3], a_li[n - 2]
    if a_li[n - 1] == b_li[n - 1] and a_li[n - 2] == b_li[n - 2] and a_li[n - 3] == b_li[n - 3]:
        flag = True
    a_li[n - 3], a_li[n - 2], a_li[n - 1] = a_li[n - 1], a_li[n - 3], a_li[n - 2]
    if a_li[n - 1] == b_li[n - 1] and a_li[n - 2] == b_li[n - 2] and a_li[n - 3] == b_li[n - 3]:
        flag = True
    if flag:
        return print('Yes')
    else:
        return print('No')

if __name__ == '__main__':
    b_arc136()
