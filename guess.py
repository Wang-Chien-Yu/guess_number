import random

x = int(input('請輸入範圍開始值: '))
y = int(input('請輸入範圍結束值: '))
r = random.randint(x, y)
count = 0

while True:	
	count += 1
	num = int(input('請輸入你猜的數字: '))	
	if num == r:
		print('恭喜你!猜對了')
		print('你總共猜了', count, '次')
		break
	elif num > r:
		print('比答案大，在猜猜看')
	elif num < r:
		print('比答案小，在猜猜看')
	print('這是你猜的第', count, '次')
	
