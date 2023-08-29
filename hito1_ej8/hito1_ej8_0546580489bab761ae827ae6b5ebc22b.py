#Descomponer un número
n = input("Ingrese un numero para descomponer: ")
n = list(int(x) for x in n)

if len(n) == 4:
    print("{0}M + {1}C + {2}D + {3}U".format(n[0], n[1], n[2], n[3]))
elif len(n) == 3:
    print("{0}C + {1}D + {2}U".format(n[0], n[1], n[2]))
elif len(n) == 2:
    print("{0}D + {1}U".format(n[0], n[1],))
elif len(n) == 1:
    print("{0}U".format(n[0]))
     