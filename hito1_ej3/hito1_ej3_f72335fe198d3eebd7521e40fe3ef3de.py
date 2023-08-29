
ing=int(input("Ingrese su sueldo líquido: "))
ano1=int(input("Ingrese su año de nacimiento: "))
ano=2021-ano1
hijos=int(input("Ingrese el número de hijos: "))
ingb=int(input("Ingrese la cantidad de años que lleva perteneciendo al banco: "))
eciv=input("Ingrese S si es soltero o C si es casado: ")
lug=input("Ingrese U si vive en sector urbano o R si vive en sector rural: ")

if ingb>10 and hijos>1:
    print("APROBADO")

elif (eciv=="c" or eciv=="C") and  hijos>2 and (ano>44 or ano<56):

    print("APROBADO")

elif ing>2499999 and ((eciv=="s" or eciv=="S") and (lug=="u" or lug=="U")):

    print("APROBADO")

elif ing>3499999 and ingb>5:

    print("APROBADO")

elif (eciv=="c" or eciv=="C") and (lug=="r" or lug=="R") and hijos<2:

     print("APROBADO")
