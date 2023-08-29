#Descomponer un número
numero=int(input("numero: "))
u=numero%10
d=numero//10
d=d%10
c=numero//100
c=c%10
m=numero//1000

print(m,"M+",c,"C+",d,"D+",u,"U")