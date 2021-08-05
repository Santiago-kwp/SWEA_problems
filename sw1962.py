'''
369 게임에서 가장 중요한, 3, 6, 9의 숫자를 카운트하여 계산하는 ct변수를 지정하여 출력
'''
N = int(input())
for i in range(1,N+1):
    ct = str(i).count('3') + str(i).count('6') + str(i).count('9')
    if (ct == 0):
        print(i, end=" ")
    else:
        print('-'*ct, end=" ")