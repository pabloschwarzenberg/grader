def mcd(a, b):
	if b==0:
		return a
	resto=a%b
	return mcd(b, resto)
def mcm(a, b, ab):
	return ab/mcd(a, b)



if __name__=="__main__":
    pass
           