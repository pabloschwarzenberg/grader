# Descomponer un número
N = (input("Ingrese un numero de hasta 4 digitos"))

if int(N) >= 1000:
    assert isinstance(N, object)
    print(N[0]+ "M +",  N[1]+ "C +",  N[2] + "D +", N[3] + "U")
elif int(N) >= 100:
    print(N[0]+ "C +",  N[1] + "D +", N[2] + "U")
elif int(N) >= 10:
    print( N[0] + "D +", N[1] + "U")
elif int(N) <=10:
    print(N[0] + "U")
