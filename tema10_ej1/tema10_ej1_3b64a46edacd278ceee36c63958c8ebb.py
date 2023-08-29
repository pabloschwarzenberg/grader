def mcm(a,b,ab):
	return((a*b)/mcd(a,b))

def mcd(a,b,i=0,div=1,divisoresa =[],divisoresb = []):
	if(i == 0):
		divisoresa = divisores(a)
		divisoresb = divisores(b)
	if(i == len(divisoresa)):
		return(div)
	else:
		if(divisoresa[i] in divisoresb):
			div = divisoresa[i]
		return(mcd(a,b,i+1,div,divisoresa.copy(),divisoresb.copy()))
	
def divisores(n,j=1,todos=[]):
	if(j > n):
		print(todos.copy())
		return(todos.copy())
	else:
		if(n%j==0):
			todos.append(j)
		return(divisores(n,j+1,todos.copy()))
if __name__=="__main__":
		pass
           