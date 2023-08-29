#Descomponer un número
n=int(input('ingrese un numero:'))
mil=n//1000
centena=(n-mil*1000)//100
decena=(n-mil*1000-centena*100)//10
unidad=(n-mil*1000-centena*100-decena*10)
if decena==0:
 print(unidad,'U')
elif centena==0:
 print(decena,'D+',unidad,'U')
elif mil==0:
 print(centena, 'C+',decena,'D+',unidad,'U')
else:
 print(mil,'M+',centena,'C+',decena,'D+',unidad,'U')