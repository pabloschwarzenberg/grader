#Descomponer un número
N = str(input("Ingrese un numero de 4 digitos: "))
C = len(N)
if C == 1:
    print(N+"U")
elif C == 2:
    print(N[0:1]+"D +",N[1:2]+"U +")
elif C == 3:
    print(N[0:1]+"C +",N[1:2]+"D +",N[2:3]+"U +")
else:
    print(N[0:1]+"M +",N[1:2]+"C +",N[2:3]+"D +",N[3:4]+"U +")