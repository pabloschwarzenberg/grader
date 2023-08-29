#Descomponer un número
numero1=input()
numero=str(numero1)
if len(numero)==4:
    a=numero[0]
    b=numero[1]
    c=numero[2]
    d=numero[3]
    print("{0}M + {1}C + {2}D + {3}U".format(a,b,c,d))
elif len(numero)==3:
    a=numero[0]
    b=numero[1]
    c=numero[2]
    print("{0}C + {1}D + {2}U".format(a,b,c))
elif len(numero)==2:
    a=numero[0]
    b=numero[1]
    print("{0}D + {1}U".format(a,b))
elif len(numero)==1:
    print(numero+U)
else:
    print("No es posible")
      