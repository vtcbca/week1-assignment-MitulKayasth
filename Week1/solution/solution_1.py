#Write a python script to enter any number and check its prime or not.

n = 9
if(n > 1):
	for k in range(2, int(sqrt(n)) + 1):
		if (n % k == 0):
			flag = 1
		break
	if (flag == 0):
		print(n," is a Prime Number!")
	else:
		print(n," is Not a Prime Number!")
else:
	print(n," is Not a Prime Number!")



