'''
딱 정해진 칸수만 있어야 들어갈 수 있으므로 
열방향 matrix 와 횡방향 tr_matrix을 만들어서 
검은색이 0 이기 때문에 양끝에 0을 추가한 임의 패딩을 만들어서 예외처리
추가로 01110을 찾는경우에서 011101110 이렇게 중첩되는 경우를 못찾길래 re 함수 사용
'''
T = int(input())
import re # process overlapping string counts

for test_case in range(1, T+1):
    n, k = map(int, input().split())
    sub = '0'+'1'*k+'0'
    word = 0
    matrix = []
    for i in range(n):
        matrix.append(''.join(input().split()))
    
    tr_matrix = []
    for i in zip(*matrix):
        tr_matrix.append(''.join(i))
    
    # find -> direc empty k space
    for row in matrix:
        word += len(re.findall(f'(?={sub})','0'+row+'0'))
    
    for row in tr_matrix:
        word += len(re.findall(f'(?={sub})','0'+row+'0'))
    
    print(f'#{test_case} {word}')