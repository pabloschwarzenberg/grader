def rut(numero):
    valor = reversed(str(numero))
    aux= 2
    suma = 0 
    for digitos in valor:
        resultado = int(digitos) * aux
        suma += resultado

        if aux == 7:
            aux= 2
        else:
            aux += 1

    print(suma)
    parte=(suma//11)
    resto = suma-(11*parte)
    dv =11-resto
    if dv == 11:
        dv = 0
    if dv == 10:
        dv = "k"

    return dv

Valorx = int(input("Mencione el numero:"))
dv= rut(Valorx)

print("dv = " , end="")
print(dv)