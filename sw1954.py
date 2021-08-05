'''
달팽이가 움직이는 칸 수의 규칙을 정한 move_len 리스트를 지정하고
이에 맞춰서 우->아래->좌->위->우->...에 맞게 dx, dy를 지정하여 2d 리스트를 만듦
'''
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    snail = [[0]*N for _ in range(N)]
    # IF N = 4 -> 시작 4칸(우) -> 3칸 2번(아래,좌) -> 2칸 2번(위,우) -> 1칸 2번(아래, 좌) 
    # move_len = [4, 3, 3, 2, 2, 1, 1]
    move_len = [N]
    while N > 1:
        move_len.extend([N-1, N-1])
        N -= 1
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    num = 1
    x, y, k = -1, 0, 0
    for move in move_len:
        for m in range(move):
            x += dx[k]
            y += dy[k]
            snail[y][x] = num
            num += 1
        if k < 3:
            k += 1
        else:
            k=0
    print(f'#{test_case}')
    for snail_row in snail:
        print(' '.join([str(i) for i in snail_row]))