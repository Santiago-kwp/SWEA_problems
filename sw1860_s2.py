# 진기의 최고급 붕어빵
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # N : 사람 수, M : 붕어빵 만드는 시간, K: 한 번에 만드는 붕어빵 수
    N, M, K = map(int, input().split())
    time = list(map(int, input().split()))
    time.sort() # 시간 순으로 정렬
    ans = 'Possible'
    for nums, t in enumerate(time,start=1):
        if (t//M)*K - nums < 0:
            ans = 'Impossible'
            break
    
    print('#{} {}'.format(tc, ans))


