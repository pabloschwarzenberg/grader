def generar(numero,largo):
  if len(numero)==largo:
    numero="".join(numero)
    print(numero)
    return
  for i in["0","1"]:
    numero.append(i)
    generar(numero,largo)
    numero.pop()
 

n=int(input("Ingresa algo: "))
generar([],n)