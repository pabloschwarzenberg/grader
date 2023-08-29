def gcd(a, b):
	t = b
	b = a % b
	if b == 0:
		return t
	else:
		return gcd(t, b)


def mcm(a,b,ab):
    return (a*b)//gcd(a,b)

if __name__=="__main__":
    pass
           