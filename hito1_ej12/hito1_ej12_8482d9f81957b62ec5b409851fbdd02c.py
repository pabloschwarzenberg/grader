import random
limite = 5
intento = 0
nrosecreto = random.randint(1 , 20)
while intento < limite :
    nro = eval(input("Ingrese un numero :"))

    if nro < nrosecreto:
        print("mi numero es mayor")
    elif nro > nrosecreto:
        print ("mi numero es menor")
    elif  nro == nrosecreto:
        print("Adivinaste, mi número era ", nrosecreto)
        break
    
    intento = intento + 1
if intento == limite:
    print ("No adivinaste, mi número era :",nrosecreto)
