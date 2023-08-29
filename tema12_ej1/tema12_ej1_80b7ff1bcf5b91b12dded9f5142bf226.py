n=int(input("Ingrese Largo numeros binarios"))

def generar(numero,largo):
    if len(numero)==largo:
        print(numero)
        return
    for d in ["0","1"]:
        numero.append(d)
        generar(numero,largo)
        numero.pop()

generar([],n)