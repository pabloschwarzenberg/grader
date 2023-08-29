#Cálculo del dígito verificador de un rut
rut=input()
rut=[int(rut[i]) for i in reversed(range(len(rut)))]
mul=list(range(2,8))*2
listos=[rut[i]*mul[i] for i in range(len(rut))]
n=sum(listos)%11
if(n==0):
	print('dv= 0')
elif(n==1):
	print('dv= k')
else:
	print('dv=',11-n)