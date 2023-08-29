#Descomponer un número
#Matías
n= int(input("Ingrese un numero de 4 digitos: ", ))

if (n<0) or (9999<n):
   print("Numero ingresado no es valido") 
if (0<n) and (n<=9):
   print(int(n // 1,),"U")
if (10<=n) and (n<=99):
   print(int(n//10),"D","+",int(n%10,1),"U")
if (100<=n) and (n<=999):
   print(int(n//100),"C","+",int((n//10)%10),"D","+",int(n%10),"U")
if (1000<=n) and (n<=9999):
   print(int(n//1000),"M","+",int((n//100)%10),"C","+",int((n//10)%10),"D","+",int((n%100)%10),"U")
else:
   print("Datos No validos")