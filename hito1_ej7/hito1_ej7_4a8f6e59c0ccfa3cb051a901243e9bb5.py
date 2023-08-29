#Zodiaco
#pide los datos

mes = int(input("ingrese el mes en que nacio: "))
dia = int(input("ingrese el dia en que nacio: "))

if mes == 12 and dia >= 22 or mes == 1 and dia <= 20:

    print("capricornio")

elif mes == 1 and dia >= 21 or mes == 2 and dia <= 18:

    print("acuarion")

elif mes == 2 and dia >= 19 or mes == 3 and dia <= 20:

    print("piscis")

elif mes == 3 and dia >= 21 or mes == 4 and dia <= 20:

    print("aries")

elif mes == 4 and dia >= 21 or mes == 5 and dia <= 21:

    print("tauro")

elif mes == 5 and dia >= 22 or mes == 6 and dia <= 21:

    print("geminis")
        
elif mes == 6 and dia >= 22 or mes == 7 and dia <= 22:

    print("cancer")

elif mes == 7 and dia >= 23 or mes == 8 and dia <= 23:

    print("leo")

elif mes == 8 and dia >= 24 or mes == 9 and dia <= 23:

    print("virgo")

elif mes == 9 and dia >= 24 or mes == 10 and dia <= 23:

    print("libra")

elif mes == 10 and dia >= 24 or mes == 11 and dia <= 22:

    print("escorpion")

elif mes == 11 and dia >= 23 or mes == 12 and dia <= 21:

    print("sagitario")

else:
    print("\nel mes o el dia que has puesto no existen\n")      