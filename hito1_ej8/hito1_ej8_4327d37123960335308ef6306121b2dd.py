#Descomponer un número
a=int(input("Ingresa un número de hasta cuatro dígitos:"))
if a>9999:
   print("Error, el número debe ser menor a 10000")
else:
    M=int((a//1000)*1000)
    c=int(a%1000)
    C=int((c//100)*100)
    d=int(a%100)
    D=int((d//10)*10)
    U=int((a%10))
if (999<a<10000):
    print((M//1000),"M + ",(C//100),"C + ",(D//10),"D + ",U,"U")
elif (99<a<1000):
    print((C//100),"C + ",(D//10),"D + ",U,"U")
elif (9<a<100):
    print((D//10),"D + ",U,"U")
else:
    print(U,"U")
