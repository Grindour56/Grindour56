n = int(input("Enter the position for which the number is to be calculated:"))
var = 0
x = 0
v = 1
y = 1
z = 0
e = 0
w = 1
if n%2 == 0:
	for k in range(2,n):
		if (n <= 3):
			var = 2
		else:
			for j in range (2,k):
				if (k%j ==0):
					v = 1
					break
				else:
					v = 0
				
		if v == 0:
			var = k
	print(var)
else:
	e = ((n+1)//2)
	x = 0
	y = 1
	z = 0
	if (e == 1): 
		print(x)
	elif (e == 2):
		print(y)
	else:
		for w in range(e+1):
			if (w >= 3):
				z = x + y 
				x = y
				y = z
		print(z)
