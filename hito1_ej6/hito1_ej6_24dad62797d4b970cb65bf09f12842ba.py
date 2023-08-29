#Ordenar tres números
nu1=int(input("Ingrese el primer numero"))
nu2=int(input("Ingrese el segundo numero"))
nu3=int(input("Ingrese el tercer numero"))
menor=0
medio=0
mayor=0
if ((nu1<=nu2) and (nu1<=nu3)):
    menor=nu1
    if (nu2<=nu3):
        medio=nu2
        mayor=nu3
    else:
        medio=nu3
        mayor=nu2
elif ((nu2<=nu1) and (nu2<nu3)):
    menor =nu2
    if (nu1<=nu3):
        medio=nu1
        mayor=nu3
    else:
        medio=nu3
        mayor=nu1
else:
    menor=nu3
    if (nu1<=nu2):
        medio=nu1
        mayor=nu2
    else:
        medio=nu2
        mayor=nu1
print(menor,",",medio,",",mayor)