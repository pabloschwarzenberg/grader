#Descomponer un número
numero = input("Ingrese Número: ")
if len(numero) == 4:
    print("{0}M + {1}C + {2}D + {3}U".format(numero[0], numero[1], numero[2], numero[3]))
elif len(numero) == 3:
    print("{0}C + {1}D + {2}U".format(numero[0], numero[1], numero[2]))
elif len(numero) == 2:
    print("{0}D + {1}U".format(numero[0], numero[1]))
elif len(numero) == 1:
    print("{0}U".format(numero[0]))      