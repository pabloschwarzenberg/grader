#Descomponer un número
numero=int(input())
a=numero//10==0
b=numero//10!=0
c=numero//100==0
d=numero//1000==0
e=numero%1000!=0
f=numero//10000==0
g=numero%10000!=0
unidad=numero%10
decena=numero//10%10
centena=numero//100%10
M=numero//1000
if a:
    print(str(numero)+"U")
elif b and c:
    print(str(decena)+"D"+"+"+str(unidad)+"U")
elif d and e:
    print(str(centena)+"C"+"+"+str(decena)+"D"+"+"+str(unidad)+"U")
    
elif f and g:
    print(str(M)+"M"+"+"+str(centena)+"C"+"+"+str(decena)+"D"+"+"+str(unidad)+"U")
else:
    print("El número debe ser de hasta 4 digitos!")
