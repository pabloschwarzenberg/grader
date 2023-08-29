#E: 3 Numeros
#S: Orden Mayor a Menor(? "con razon no me tomaba..Yeet this!"

N1 = int(input("Ingrese un número:"))
N2 = int(input("Ingrese un número:"))
N3 = int(input("Ingrese un número:"))
if (N1>N2>N3):
    print(N3,",",N2,",",N1)
elif(N2>N1>N3):
    print(N3,",",N1,",",N2)
elif(N3>N2>N1):
    print(N1,",",N2,",",N3)
elif(N3>N1>N2):
    print(N2,",",N1,",",N3)
elif(N1>N3>N2):
    print(N2,",",N3,",",N1)
elif(N2>N3>N1):
    print(N1,",",N3,",",N2)
elif(N1==N2>N3):
    print(N3,",",N2,",",N1)
elif(N2==N1>N3):
    print(N3,",",N1,",",N2)
elif(N3==N2>N1):
    print(N1,",",N2,",",N3)
elif(N3==N1>N2):
    print(N2,",",N1,",",N3)
elif(N1==N3>N2):
    print(N2,",",N3,",",N1)
elif(N2==N3>N1):
    print(N1,",",N3,",",N2)
elif(N1>N2==N3):
    print(N3,",",N2,",",N1)
elif(N2>N1==N3):
    print(N3,",",N1,",",N2)
elif(N3>N2==N1):
    print(N1,",",N2,",",N3)
elif(N3>N1==N2):
    print(N2,",",N1,",",N3)
elif(N1>N3==N2):
    print(N2,",",N3,",",N1)
elif(N2>N3==N1):
    print(N1,",",N3,",",N2)
elif(N1==N2==N3):
    print(N3,",",N2,",",N1)