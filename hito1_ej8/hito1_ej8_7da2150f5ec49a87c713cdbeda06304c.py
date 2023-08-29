numero=int(input("Ingrese un numero: "))
m=int(numero//(10**3))
c=int((numero//(10**2))-(m*10))
d=int((numero//(10**1))-(m*100+c*10))
u=int((numero//(10**0))-(m*1000+c*100+d*10))
if numero>9999:
 print("Incorrecto")
elif 999<numero<=9999:
 print(m,"M+",+c,"C+",+d,"D+",+u,"U")
elif 99<numero<=999:
 print(c,"C+",d,"D+",u,"U")
elif 9<numero<=99:
 print(d,"D+",u,"U")
elif 0<numero<=9:
 print(u,"U")
