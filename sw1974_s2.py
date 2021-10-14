# 스도쿠 검증
import sys
sys.stdin = open('input.txt')

def sudoku(arr):
    # box 검사
    cntb = [[0]*10 for _ in range(9)]
    for i in range(9):
        cntr = [0]*10
        cntc = [0]*10
        for j in range(9):
            # 가로 검사
            if not cntr[arr[i][j]]: 
                cntr[arr[i][j]] = 1
            else:
                return 0
            # 세로 검사
            if not cntc[arr[j][i]]: 
                cntc[arr[j][i]] = 1
            else:
                return 0
            # 3x3 박스 검사
            ibox = 3*(i//3) + (j//3)
            if not cntb[ibox][arr[i][j]]:
                cntb[ibox][arr[i][j]] = 1
            else:
                return 0
    return 1
            
T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    print('#{} {}'.format(tc, sudoku(arr)))