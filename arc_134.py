def division(x, y) -> int:
    if x % y == 0:
        return x // y
    else:
        return x // y + 1


def a_arc134():
    cnt = 0
    _, length, width = map(int, input().split())
    s_bridges = list(map(int, input().split()))
    pt = 0
    for bridge in s_bridges:
        if pt < bridge:
            cnt += division(bridge - pt, width)
        # print(f"cnt: {cnt} pt: {pt} bridge: {bridge}")
        pt = bridge + width
    if pt < length:
        cnt += division(length - pt, width)
    return print(cnt)


def swap(li: list, i: int, j: int):
    tmp = li[i]
    li[i] = li[j]
    li[j] = tmp


def b_arc134():
    pt = int(input()) - 1
    s_li = list(input())
    s_set_sorted = sorted(set(s_li))
    s_li_index = []
    left = 0
    for c_set in s_set_sorted:
        for i in range(pt, -1, -1):
            if s_li[i] == c_set:
                s_li_index.append(i)
                if s_li[left] > s_li[i]:
                    swap(s_li, left, i)
                pt = i
    pt = 0
    for index in s_li_index:
        while True:
            # if pt >= n:
            #     break
            if pt >= index:
                break
            #print(s_li)
            if s_li[pt] > s_li[index]:
                # print(f"swapped {s_li[pt]} {s_li[index]}")
                swap(s_li, pt, index)
                break
            pt += 1

    return print("".join(s_li))
    #print(s_li_index)
    #print(s_set_sorted)


if __name__ == '__main__':
    b_arc134()