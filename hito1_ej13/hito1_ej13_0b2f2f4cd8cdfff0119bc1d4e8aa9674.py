#Factores Primos
    #Factores Primos
def FPrimos(nro):
	
	factor=2

	while factor<=nro:
		
		if nro % factor == 0:
			
			print(factor)
			nro = nro // factor
			
		else:
			
			factor+=1

nro=int(input())

FPrimos(nro)  