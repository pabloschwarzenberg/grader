c1=int(input("Inserte la cantidad de votos de la 1ra comuna: "))
c2=int(input("Inserte la cantidad de votos de la 2da comuna: "))
c3=int(input("inserte la cantidad de votos de la 3ra comuna: "))
tvotos=c1+c2+c3
v1=int(input("Inserte la cantidad de votos de la Senadora en la 1ra comuna: "))
while (v1>c1):
    v1=int(input("La cantidad de votos de la Senadora no pueden ser mayores que los de la comuna, Intente nuevamente: "))
    if(c1>v1):
        break
    else:
        continue
v2=int(input("Inserte la cantidad de votos de la Senadora en la 2da comuna: "))
while (v2 > c2):
    v2=int(input("La cantidad de votos de la Senadora no pueden ser mayores que los de la comuna, Intente nuevamente: "))
    if(c2>v2):
        break
v3 = int(input("Inserte la cantidad de votos de la Senadora en la 3ra comuna: "))
while (v3>c3):
    v3=int(input("La cantidad de votos de la Senadora no pueden ser mayores que los de la comuna, Intente nuevamente: "))
    if(c3>v3):
        break
vsenadora=v1+v2+v3
v2senadora=v1+v2
v3senadora=v1+v3
v4senadora=v2+v3
if((v1*100)/c1>=80):
    print("La Senadora Isabel obtuvo la cantidad de votos necesarios para ser electa tan solo con la primera comuna, lo que corresponde a : %"+str((v1*100)/c1)+ "De los votos.")
elif((((v2senadora*100)/tvotos)>=70) or (((v3senadora*100)/tvotos)>70) or (((v4senadora*100)/tvotos))>70):
    print("La Senadora Isabel obtuvo la cantidad de votos necesarios para ser electa con solo 2 comunas.")
elif(((vsenadora*100)/tvotos)>=40):
    print("La Senadora Isabel fue electa en las elecciones conjunto a las 3 comunas con un total de : %"+str((vsenadora*100)/tvotos)+" de los votos.")
else:
    print("La Senadora Isabel resulto perdedora")