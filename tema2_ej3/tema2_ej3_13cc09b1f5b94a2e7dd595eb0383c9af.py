def numero_perfecto(Valor):
    Total = 0
    Lista = []
    for Numero in range(1, Valor):
        if (Valor%Numero == 0):
             Lista.append(Numero)
    for Numero in Lista:
        Total += Numero
    if (Total == Valor):
        return True
    else:
        return False

print(numero_perfecto(6))