#Descomponer un número

numero=int(input("Ingrese un numero:"))

Mil = int(numero / 1000)
tmp = numero % 1000

Cen = int(tmp / 100)
tmp = tmp % 100

Dec  = int(tmp / 10)

Uni = int(tmp % 10)

if int(Mil)!=0:
    
    print(" {Mil} M + {Cen} C + {Dec} D + {Uni} U",sep="+")

elif int(Mil)==0 :
    print(" {Cen} C + {Dec} D + {Uni} U",sep="+")

else:
    print("{Dec} D + {Uni} U",sep="+")