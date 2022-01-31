def a_237():
    n = int(input())
    if -1 * (2**31) <= n < (2**31):
        return print('Yes')
    else:
        return print('No')

def b_237():
    h, _ = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(h)]
    for j in range(len(li[0])):
        for i in range(len(li)):
            print(li[i][j], end=' ')
        print()

def c_237():
    s = list(input())
    i = 0
    while s[len(s) - 1 - i] == 'a':
        i += 1
        if i > len(s):
            break
    if not s:
        return print('Yes')
    # print(s)
    j = 0
    while s[j] == 'a' and j < i:
        j += 1
        if j >= len(s):
            break
    s = s[j:len(s) - i]
    # print(s)
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return print('No')
    return print('Yes')

# TLE
def d_237():
    n = int(input())
    s = input()
    ans = [0]
    pt = 0
    l_num = 0
    r_num = 0
    i = 1
    while i <= n + 1:
        if i == n + 1:
            if l_num:
                ans = ans[:pt] + [j for j in range(i - 1, i - l_num - 1, -1)] + ans[pt:]
            if r_num:
                ans = ans[:pt + 1] + [j for j in range(i - r_num, i)] + ans[pt + 1:]
            break
        if s[i - 1] == 'L':
            l_num += 1
            if r_num:
                ans = ans[:pt + 1] + [j for j in range(i - r_num, i)] + ans[pt + 1:]
                pt += r_num
                r_num = 0
            # print(ans)

        else:
            r_num += 1
            if l_num:
                ans = ans[:pt] + [j for j in range(i - 1, i - l_num - 1, -1)] + ans[pt:]
                l_num = 0
            # print(ans)
        i += 1
    print(*ans)

def e_237():
    pass


if __name__ == '__main__':
    b_237()