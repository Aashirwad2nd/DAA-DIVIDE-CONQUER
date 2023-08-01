# gcd using recursion

def gcd(a, b):
	if(b == 0):
		return abs(a)
	else:
		return gcd(b, a % b)

a = 270
b = 192

x = gcd(270, 192)
print(f"The gcd of {a} and {b} is : ",x)




