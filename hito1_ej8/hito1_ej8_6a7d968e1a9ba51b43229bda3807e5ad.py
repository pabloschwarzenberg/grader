#Descomponer un número
numero=int(input("Ingrese un numero: "))

m=((numero//1000)%10)
c=((numero//100)%10)
d=((numero//10)%10)
u=((numero//1)%10)

if numero <= 9999 and numero >= 1000:
    print(m,"M + ",c,"C + ",d,"D + ",u,"U")
elif numero <= 999 and numero >= 100:
    print(c,"C + ",d,"D + ",u,"U")
elif numero <= 99 and numero >= 10:
    print(d,"D + ",u,"U") 
elif numero <=9 and numero >= 0:
    print(u,"U")
else:
    print("No es posible con este numero.")