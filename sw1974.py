'''
스도쿠를 검증하기 위해 열과 행의 총합, 그리고 3x3 행렬의 총합이 45인지 각각 확인하는
pan_check 함수를 만들어서 풀이
'''
def pan_check(pan):
    for row in pan:
        if sum(row) != 45:
            return 0
            
    for col in zip(*pan):
        if sum(col) != 45:
            return 0
            
    for c in range(0,9,3):
        for r in range(0,9,3):
            if sum(pan[r][c:c+3]+pan[r+1][c:c+3]+pan[r+2][c:c+3]) != 45:
                return 0
    return 1    

T = int(input())

for test_case in range(1,T+1):
    pan = [list(map(int,input().split())) for _ in range(9)]

    print(f'#{test_case} {pan_check(pan)}')