def FactoresPrimos(n):
	
	f=2

	while f<=n:
		
		if n % f == 0:
			
			print(f)
			n = n // f
			
		else:
			
			f+=1

n=int(input())

FactoresPrimos(n)     