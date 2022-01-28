from math import sqrt


def b_105(n=int(input())):
    total_count = 0
    for i in range(1, n + 1, 2):
        cnt = 0
        for j in range(1, int(sqrt(i)) + 2, 2):
            if i % j == 0:
                cnt += 2
        if cnt == 8:
            total_count += 1
    return print(total_count)


if __name__ == '__main__':
    b_105()
