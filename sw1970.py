'''
욕심쟁이 알고리즘의 문제로 큰 거스름돈부터 차례로 나눗셈 몫을 이용하여 
필요한 개수를 새고 리스트에 저장
'''
moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for t in range(int(input())):
    total = int(input())
    money_list = []
    for m in moneys:
        money_list.append(total//m)
        if total//m:
            total -= m*(total//m)
    print(f'#{t+1}')
    print(*money_list)  