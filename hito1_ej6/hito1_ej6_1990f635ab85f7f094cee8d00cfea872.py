#Ordenar tres números
X = int(input("Primer numero:"))
Y = int(input("Segundo numero:"))
Z = int(input("Tercer numero:"))
if X >= Y and Y >= Z:
    print(Z,",", Y,",", X)
else:
    if Y >= X and X >= Z:
        print(Z,",", X,",", Y)
    else:
        if X >= Z and Z >= Y:
            print(Y,",", Z,",", X)
        else:
            if Z >= X and X >= Y:
                print(Y,",", X,",", Z)
            else:
                if Z >= Y and Y >= X:
                    print(X,",", Y,",", Z)
                else:
                    Y >= Z and Z >= X
                    print(X,",", Z,",", Y)