#Ordenar tres números
n1=int(input("ingrese numero 1 :"))
n2=int(input("ingrese numero 2 :"))
n3=int(input("ingrese numero 3 :"))
numero_mayor=0
numero_menor=1000000000000000000000000000000000000
numero_medio=0
if n1 > numero_mayor:
    numero_mayor=n1
if n2> numero_mayor:
    numero_mayor=n2
if n3> numero_mayor:
    numero_mayor=n3
#___________________________
if n1 < numero_menor:
    numero_menor=n1
if n2< numero_menor:
    numero_menor=n2
if n3< numero_menor:
    numero_menor=n3
#___________________________

if n1==numero_mayor and n2==numero_menor:
    numero_medio=n3
if n2==numero_mayor and n1==numero_menor:
    numero_medio=n3
if n3==numero_mayor and n1==numero_menor:
    numero_medio=n2
if n1==numero_mayor and n3==numero_menor:
    numero_medio=n2
if n3==numero_mayor and n2==numero_menor:
    numero_medio=n1
if n2==numero_mayor and n3==numero_menor:
    numero_medio=n1




    
print(numero_menor,",",numero_medio,",",numero_mayor)   