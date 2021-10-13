import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input().split())) for _ in range(N)]

# 횡축으로 이등분하는 인덱스의 범위는 idx : 1 ~ N-1
# 4등분 하여 a, b, c, d 로 나누고 a, c, b+d 3구역으로 나눔
    min_diff = 9*N**2
    for i in range(1, N):                   # 횡으로 이등분
        for j in range(N-1):
            a = b = c = d = 0
            for k in range(j+1):            # 종으로 이등분
                a += sum(farm[k][:i])
                b += sum(farm[k][i:])
                # print(farm[k][:i], farm[k][i:])
            # print(a, b)
            # print('-----------------------')
            for l in range(j+1, N):         
                c += sum(farm[l][:i]) 
                d += sum(farm[l][i:])
                # print(farm[l][:i], farm[l][i:])
            # print(c, d)
            # print('-----------------------')
            loc = [a, c, b+d]
            # print(loc)
            diff = max(loc)-min(loc)
            min_diff = min(min_diff, diff)
    print('#{} {}'.format(tc, min_diff))
