import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 연속적으로 1이 되는 경우를 찾자
    match = 0
    for i in range(N):
        cnt = cntc =  0
        for j in range(N):
            # 가로 검사       
            if arr[i][j]:
                cnt += 1
            else:
                if K == cnt:
                    match += 1
                cnt = 0
            # 세로 검사
            if arr[j][i]:
                cntc += 1
            else:
                if K == cntc:
                    match += 1
                cntc = 0
        if K == cntc:
            match += 1
        if K == cnt:
            match += 1
    print('#{} {}'.format(tc, match))