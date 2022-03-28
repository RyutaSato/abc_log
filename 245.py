import tkinter.tix


def a():
    a, b, c, d = map(int, input().split())
    ans = 'Takahashi'
    if a < c:
        return print(ans)
    elif a == c:
        if b <= d:
            return print(ans)
        else:
            return print('Aoki')
    else:
        return print('Aoki')

def b():
    _ = input()
    li = list(map(int, input().split()))
    li.sort()
    nums = list(range(0,2001))
    for i in li:
        if i in nums:
            nums.remove(i)
    return print(nums[0])

def rec(ans:list, a_li:list, b_li:list, n, i, k):
    if ans:
        ans.append(a_li[0])
        ans = rec(ans, a_li, b_li, n, i + 1, k)
        if len(ans) == n:
            return ans
        else:
            ans.pop()
            ans.append(b_li[0])
            ans = rec(ans, a_li, b_li, n, i + 1, k)
            if len(ans) == n:
                return ans
        return []
    if abs(ans[-1] - a_li[i]) <= k:
        ans.append(a_li[i])
    elif abs(ans[-1] - b_li[i]) <= k:
        ans.append(b_li[i])
    else:
        ans.pop()
        i -= 1
    return rec(ans, a_li, b_li, n, i, k)

def c():
    n, k = map(int, input().split())
    a_li = list(map(int, input().split()))
    b_li = list(map(int, input().split()))
    ans = []
    i = 0
    t_li = [0] * n # 1 -> a 2-> b 0 -> no answer
    while i < n:
        print(f"ans:{ans} tli:{t_li} i:{i}")
        if not ans:
            if t_li[0] == 0:
                ans.append(a_li[i])
            elif t_li[0] == 1:
                ans.append(b_li[i])
            else:
                return print('No')
            t_li[i] += 1
            i += 1
            continue
        if t_li[i] == 0 and abs(ans[i-1] - a_li[i]) <= k:
            ans.append(a_li[i])
        elif t_li[i] == 1 and abs(ans[i-1] - b_li[i]) <= k:
            ans.append(b_li[i])
        elif t_li[i] < 2:
            t_li[i] += 1
            continue
        else:
            ans.pop()
            i -= 1

        i += 1
    print(t_li)
    print(ans)
    return print('Yes')

if __name__ == '__main__':
    c()