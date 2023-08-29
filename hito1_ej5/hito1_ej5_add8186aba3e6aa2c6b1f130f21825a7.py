#IMPRIMIR EL NÚMERO VERIFICADOR DE UN RUT

#entradas
RUT = int(input("Ingrese su RUT aquí sin el código verificador: "))

#variables XX.XXX.XXX
#          87 654 321

##Sacar dígito de cada rut
X1 = (RUT//1)%10
X2 = (RUT//10)%10
X3 = (RUT//100)%10
X4 = (RUT//1000)%10
X5 = (RUT//10000)%10
X6 = (RUT//100000)%10
X7 = (RUT//1000000)%10
X8 = (RUT//10000000)%10

##Multiplicarlos con el patron indicado:
p1 = X1 * 2
p2 = X2 * 3
p3 = X3 * 4
p4 = X4 * 5
p5 = X5 * 6
p6 = X6 * 7
p7 = X7 * 2
p8 = X8 * 3

##sumar los productos
suma = p1 + p2 + p3 + p4  + p5 + p6 + p7 + p8


##sacar el módulo y restarlo a 11 para asi obtener el verif.
resto = suma%11
verificador = 11 - resto

if verificador == 10:
    print("dv=K")
elif resto == 0:
    print("dv=0")

else:
    print("dv="+str(verificador))