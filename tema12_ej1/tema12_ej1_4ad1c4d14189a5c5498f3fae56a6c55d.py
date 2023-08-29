
def generar(numero,largo):
    if len(numero)==largo:
        print(numero)
        return
    else:
        for d in ["0","1"]:
            numero.append(d)
            generar(numero,largo)
            numero.pop()

n=int(input())
generar([],n)

           