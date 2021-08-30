import sys
sys.stdin = open("s_input.txt")
'''
Brute-force로 Ai * Aj 의 경우를 구하는 
danjo함수와 단조증가를 체크하는 check 함수를 정의하여 풀이
'''
def check(a):
    n = 10
    while a:
        if a%10 <= n:
            a, n = divmod(a,10)
        else:
            return 0
    return 1

def danjo(An):
    max_n = -1
    for i in range(len(An)):
        for j in range(i+1,len(An)):
            a = An[i] * An[j]
            if check(a):
                if max_n < a:
                    max_n = a
    return max_n

for tc in range(1, int(input())+1):
    N = int(input())
    An = list(map(int, input().split()))
    print('#{} {}'.format(tc, danjo(An)))
