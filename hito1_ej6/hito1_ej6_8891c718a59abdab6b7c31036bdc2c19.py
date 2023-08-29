#Ordenar tres números
print("Ingresar 3 números")

A=eval(input("Ingrese un número: "))
B=eval(input("Ingrese un número: "))
C=eval(input("Ingrese un número: "))

if((A<=B) and (A<=C)):
    MENOR=A
    if (B<C):
     MEDIO=B
     MAYOR=C
    else:
        MEDIO=C
        MAYOR=B

elif((B<=A) and (B<=C)):
    MENOR=B
    if (A<C):
     MEDIO=A
     MAYOR=C
    else:
        MEDIO=C
        MAYOR=A

else:   
    MENOR= C
    if (A<B):
     MEDIO=A
     MAYOR=B
    else:
        MEDIO=B
        MAYOR=A

print("El orden es: ",MENOR,",",MEDIO,",",MAYOR)

