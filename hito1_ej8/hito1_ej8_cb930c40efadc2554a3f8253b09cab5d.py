#Descomponer un número
numero=int(input("Ingrese un numero que no pase de los miles: "))
def unidades(x):
    miles=x//1000
    j=x-(miles*1000)
    centenas=j//100
    y=j-(centenas*100)
    decenas=y//10
    unidades=x%10
    if miles>0:
        print(miles,"M +", centenas,"C +", decenas,"D +", unidades,"U")   
    elif miles==0 and centenas>=1:
        print(centenas,"C +", decenas,"D +", unidades,"U")
    elif miles==0 and centenas==0:
        print(decenas,"D +", unidades,"U")
    elif miles==0 and centenas==0 and decenas==0:
        print(unidades,"U")     
unidades(numero)