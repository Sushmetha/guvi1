c=int(input())
d=int(input())
if c and d < 10000:
	for i in range(c,d+1):
		if i % 2!=0:
			print(i)
