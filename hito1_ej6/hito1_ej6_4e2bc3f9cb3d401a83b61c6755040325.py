valor=eval(input("Ingrese un valor: "))
valor2=eval(input("Ingrese un segundo valor: "))
valor3=eval(input("Ingrese un tercer valor: "))
if ((valor <= valor2 ) and (valor <= valor3)):
    menor = valor;
    if (valor2 <= valor3):
        medio=valor2
        mayor=valor3
    else:
        medio=valor3
        mayor=valor2
elif((valor2<=valor) and (valor2<valor3)):
    menor=valor2
    if(valor<=valor3):
        medio=valor
        mayor=valor3
    else:
        medio=valor3
        mayor=valor
else:
    menor=valor3
    if(valor <= valor2):
        medio=valor
        mayor=valor2
    else:
        medio=valor2
        mayor=valor
print(str(menor),",",str(medio),",",str(mayor))