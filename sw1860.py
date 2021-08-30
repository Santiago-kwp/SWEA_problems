import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    sonim = list(map(int, input().split()))
    sonim.sort()
    c = bread = 0
    ans = 1
    for t in sonim:
        c += 1                      # 손님이 한명씩 오면
        if t//M:                    # 빵이 나오는 쿨타임에 몫이 1 이상이면
            bread = K*(t//M) - c    # 남은 빵 = 빵의 개수 - c 손님 수
        else:                       # 몫이 1 이하면 빵 부족
            ans = 0
            break
        if bread < 0:               # 남은 빵이 0 이하면 빵 부족
            ans = 0
            break

    print('#{} {}'.format(tc, 'Possible' if ans else 'Impossible'))
