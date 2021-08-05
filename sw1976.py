'''
시와 분 중 분이 60분을 초과하는 경우에 시를 추가하고 
그 다음 시가 12를 초과하는 경우를 맞춰 로직 순서를 알맞게 정해야 하는 문제
'''
T = int(input())
for test_case in range(1,T+1):
    times = list(map(int, input().split()))
    h = times[0] + times[2]
    m = times[1] + times[3]
    if m > 59:
        h += 1
        m -= 60
    if h > 12:
        h -= 12
    print(f'#{test_case} {h} {m}')