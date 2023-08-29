#Descomponer un número
numero = int(input("Ingrese Numero: "))
a=str(numero)
if numero/100 <10:
    print(a[:1]+"C","+",a[1:2]+"D","+",a[-1:]+"U")
else:
    print(a[:1]+"M","+",a[1:2]+"C","+",a[2:3]+"D","+",a[-1:]+"U")
             

             
                   