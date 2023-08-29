numero1=int(input("ingrese un numero:"))
numero2=int(input("ingrese un numero:"))
numero3=int(input("ingrese un numero:"))
a=0
b=0
c=0
if (numero1 <= numero2 and numero1 <= numero3):
    a=numero1
    if (numero2>=numero3):
        c=numero2
        b=numero3
    else:
        c=numero3
        b=numero2
print("La lista de numeros es",a,",",b,",",c)