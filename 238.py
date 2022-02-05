def a_238():
    n = int(input())
    if 1 << n > n ** 2:
        return print('Yes')
    else:
        return print('No')

def b_238():
    n = int(input())
    li = list(map(int, input().split()))
    p = 0
    cut_list = [0]
    for i in li:
        p = (p + i) % 360
        cut_list.append(p)
    cut_list.sort()
    max_rad = 0
    for i in range(1, len(cut_list)):
        if i == len(cut_list) - 1 and max_rad < cut_list[0] + 360 - cut_list[i]:
            max_rad = cut_list[0] + 360 - cut_list[i]
        else:
            if max_rad < cut_list[i] - cut_list[i - 1]:
                max_rad = cut_list[i] - cut_list[i - 1]
    return print(max_rad)


def c_238():
    n = int(input())
    ans = 0
    digit = 0
    while n // (10 ** digit) != 0:
        digit += 1
    digit -= 1
    ans += (n - (10 ** digit)+1) * (n - (10 ** digit) + 2) // 2
    if digit >= 1:
        ans += 45
        while digit > 1:
            # print(ans)
            ans += ((10 ** digit) - (10 ** (digit - 1))) * ((10 ** digit) - (10 ** (digit - 1)) + 1) // 2
            digit -= 1
    return print(ans % 998244353)



def d_238():
    n = int(input())
    for _ in range(n):
        a, s = map(int, input().split())
        i, same, not_same, max_i = 0, 0, 0, 0
        while s > 1 << i:
            if a & 1 << i:
                same |= 1 << i
            else:
                not_same |= 1 << i
                max_i = i
            i += 1
        print(a, s, same, not_same, i)
        if 2 * same == s:
            print('Yes')
            continue
        elif 2 * same > s:
            print('No')
            continue
        i = 0
        flag = 0
        is_ans = False
        while i < 62:
            if not_same & 1 << i:
                tmp = 2 * same | (not_same & 1 << i) | flag
                if tmp > s:
                    while i > 0:
                        i -= 1
                        if flag & 1 << i:
                            tmp = 2 * same | (flag ^ (1 << i))
                            if tmp > s:
                                flag ^= 1 << i
                            elif tmp == s:
                                is_ans = True
                                break
                    break
                elif tmp == s:
                    is_ans = True
                    break
                else:
                    flag |= (not_same & 1 << i)
                    flag |= (not_same & 1 << i)
            i += 1
        print('Yes') if is_ans else print('No')



if __name__ == '__main__':
    d_238()