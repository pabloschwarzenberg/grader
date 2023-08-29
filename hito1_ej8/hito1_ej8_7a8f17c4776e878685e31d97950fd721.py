#Descomponer un númeronumero
numero = int(input('Ingrese un numero de 4 DIGITOS: '))
m=(numero//1000)
c=((numero//100)%10)
d=((numero//10)%10)
u=(numero%10)

print(str (m)+'M + '+str (c)+'C + '+str (d)+'D + '+str (u)+'U')