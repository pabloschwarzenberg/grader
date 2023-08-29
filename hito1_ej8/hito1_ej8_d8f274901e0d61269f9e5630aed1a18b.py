#Descomponer un número
x = int(input("Escriba un número de hasta 4 cifras: "))
L = ["M","C","D","U"]

#Descomponer en Unidades
a = ((x//1000)%10)
b = ((x//100)%10)
c = ((x//10)%10)
d = ((x//1)%10)

#Definir cada unidad [+50 puntos de estilo]
primera_unidad = L[0]
segunda_unidad = L[1]
tercera_unidad = L[2]
cuarta_unidad = L[3]

#Condicionantes de print
if a > 0:
    print(a,primera_unidad,"+",b,segunda_unidad,"+",c,tercera_unidad,"+",d,cuarta_unidad,sep="")

else:
    if b > 0:
        print(b,segunda_unidad,"+",c,tercera_unidad,"+",d,cuarta_unidad,sep="")

    else:
        if c > 0:
            print(c,tercera_unidad,"+",d,cuarta_unidad,sep="")

        else:
            if d > 0:
                print(d,cuarta_unidad,sep="")

            else:
                print("0")
