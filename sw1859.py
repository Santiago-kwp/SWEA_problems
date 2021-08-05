'''
미래를 본다는 것 = 뒤에 나올 숫자부터 확인해서 최대값을 지정하고
뒤보다 작은 경우 이익에 더하고 아닌 경우 최대값을 변경 하는 접근 방식
'''
T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    costs = list(map(int,input().split()))
    maxc = costs[-1] 
    gain = 0
    for i in costs[::-1]:
        if maxc > i:
            gain += maxc - i
        else:
            maxc = i
            
    print(f'#{test_case} {gain}')