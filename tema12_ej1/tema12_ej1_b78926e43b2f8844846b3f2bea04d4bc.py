opciones=0,1
def generar(numero,largo):
    if len (numero)==largo:
        print(numero)
        return
    for d in opciones:
        numero.append(d)
        generar(numero,largo)
        numero.pop()
n=int(input())
generar([],n)