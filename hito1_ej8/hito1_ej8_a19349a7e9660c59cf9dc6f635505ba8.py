#Descomponer un número
numero = int(input('Ingrese un numero '))
unidades = numero%10
decenas = int(((numero%100)-unidades)/10)
centenas = int(((numero%1000)-((decenas*10)+unidades))/100)
mil = int((numero-((centenas*100)+(decenas*10)+unidades))/1000)
print('El numero tiene ', mil,'M + ',centenas,'C + ',decenas,'D + ', unidades,'U')      