numero = input("Ingrese un número de hasta 4 dígitos:")
if(eval(numero) < 10000 and eval(numero) >= 1000):
    M = numero[0]+"M"
    C = numero[1]+"C"
    D = numero[2]+"D"
    U = numero[3]+"U"
    print(M +"+" + C +"+"+ D +"+"+ U)
if(eval(numero) < 1000 and eval(numero) >= 100):
    C = numero[0]+"C"
    D = numero[1]+"D"
    U = numero[2]+"U"
    print(C + "+" + D + "+" + U)
if(eval(numero) < 100 and eval(numero) >= 10):
    D = numero[0]+"D"
    U = numero[1]+"U"
    print(D + "+" + U)
if(eval(numero) < 10 and eval(numero) >= 0):
    U = numero[0]+"U"
    print(U)
