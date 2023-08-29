#Ordenar tres números
nro=eval(input("Ingrese un valor: "))
nro2=eval(input("Ingrese un segundo valor: "))
nro3=eval(input("Ingrese un tercer valor: "))
if ((nro <= nro2 ) and (nro <= nro3)):
    menor = nro;
    if (nro2 <= nro3):
        medio=nro2
        mayor=nro3
    else:
        medio=nro3
        mayor=nro2
elif((nro2<=nro) and (nro2<nro3)):
    menor=nro2
    if(nro<=nro3):
        medio=nro
        mayor=nro3
    else:
        medio=nro3
        mayor=nro
else:
    menor=nro3
    if(nro <= nro2):
        medio=nro
        mayor=nro2
    else:
        medio=nro2
        mayor=nro
print(str(menor),",",str(medio),",",str(mayor))