'''
ssafy 입과 전 멋모르고 풀었던 문제...2x2 타일로 떼우는 경우를 '.'로 바꿔서 점층적으로 
다떼울 수 있는지 하나하나 체크하는 함수를 만들어서 풀이하였다.
'''
T = int(input())
def find_broken_tile(tile_list,m):
	try:
		for i in range(len(tile_list)):
			sind = tile_list.index('#')
			try:
				if ( (tile_list[sind+1] == '#') and (tile_list[sind+m] == '#') and (tile_list[sind+m+1] == '#') ):
					tile_list[sind] ='.'; tile_list[sind+1] = '.'; tile_list[sind+m] = '.'; tile_list[sind+m+1] = '.';
					continue
				else:
					return False
			except:
				return False
	except:
		return True

ans = []
for test_case in range(1,T+1):
	n, m = map(int,input().split())
	tile = []
	tile_list = []
	for i in range(n):
		tile.append(input())

	tile_list = [tile[i][j] for i in range(0,len(tile)) for j in range(len(tile[i]))]
    
	if (find_broken_tile(tile_list,m)):
		ans = 'YES'
	else:
		ans = 'NO'
	print('#'+str(test_case),ans)