'''
MxM 파리채를 이용해 이중 for문을 돌면서 
가장 큰 값을 찾아 지정
'''
T = int(input())
for test_case in range(1,T+1):
    N, M = map(int, input().split())
    fly = [list(map(int,input().split())) for _ in range(N)]

    imsi_sum = 0
    max_sum = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            imsi_sum = 0
            for k in range(M):
                imsi_sum += sum(fly[i+k][j:j+M])
        
            if (max_sum < imsi_sum):
                max_sum = imsi_sum
        
    print(f'#{test_case} {max_sum}')