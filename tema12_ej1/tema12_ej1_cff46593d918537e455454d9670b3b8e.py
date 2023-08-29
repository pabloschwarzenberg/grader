#Combinaciones de números binarios
#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
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