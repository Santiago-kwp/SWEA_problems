import sys
sys.stdin = open("input.txt")
'''
횡으로 순회하면서 1 찾으면 스택에 넣고, 2를 찾으면 pop 하고 교착상태 + 1
'''
for tc in range(1, 11):
    W = int(input())
    table = [list(map(int, input().split())) for _ in range(W)]
    cnt = 0 # 교착 상태의 개수
    for i in range(W):
        stack = []
        for j in range(W):
            if not stack:
                if table[j][i] == 1:
                    stack.append(1)
            else:
                if table[j][i] == 2:
                    stack.pop()
                    cnt += 1
    print('#{} {}'.format(tc, cnt))
