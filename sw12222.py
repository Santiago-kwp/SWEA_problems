'''
리스트 순서대로 하려니 예상되는 반례가 계속 생겨서
뒤에서부터 반복문을 돌려 
if 마지막 문자와 바로 전 문자가 같은 경우 
    if 지금이 처음 문자면 같이 합쳐 버리고 다음 리스트로 
    else 처음 문자가 아니면 다음 2개를 붙여버리고 2개 다음 리스트로
else 문자가 다른 경우는 바로 하나만 해서 리스트에 추가

근데 내 생각에는 테스트케이스가 부족한거 아닐까하는..?
'''
T = int(input())
for test_case in range(1,T+1):
    case = input()
    ss = [case[-1]]
    i=len(case)-2

    while(i>-1):
        if ss[-1] == case[i]:
            if i == 0:
                ss[-1] += case[i]
                i -= 1
            else:
                ss.append(case[i-1:i+1])
                i -= 2
        else:
            ss.append(case[i])
            i -= 1
    print(f'#{test_case} {len(ss)}')