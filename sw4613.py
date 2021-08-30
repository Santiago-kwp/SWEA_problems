import sys
sys.stdin = open("sample_input.txt")

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    min_cnt = N*M   # 최소 변경 깃발 개수 초기화

                                        # 흰, 파, 빨 가능한 행의 경우의 수
    for i in range(N-2):                # 흰색은 0 ~ N-3 열까지
        for j in range(i+1, N-1):       # 파랑은 1 ~ N-2 열까지, 빨강은 나머지 아래 열
            cnt = 0                     # 경우의 수에 따른 색칠 개수 초기화
            for m in range(M):
                for ii in range(i+1):       # 0~ i 열까지 흰색
                    if arr[ii][m] != 'W':
                        cnt += 1
                for jj in range(i+1, j+1):  # i+1열 ~ j열까지 파랑
                    if arr[jj][m] != 'B':
                        cnt += 1
                for k in range(j+1, N):     # 빨강은 나머지
                    if arr[k][m] != 'R':
                        cnt += 1
            if min_cnt > cnt:
                min_cnt = cnt

    print('#{} {}'.format(tc, min_cnt))

