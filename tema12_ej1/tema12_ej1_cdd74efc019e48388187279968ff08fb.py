#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar

#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
print("0000")
def generar(numero,largo):
  if len(numero)==largo:
    numero="".join(numero)
    print(numero)
    return
  for i in["0","1"]:
    numero.append(i)
    generar(numero,largo-1)
    numero.pop()

n=int(input("Ingresa algo: "))
generar([],n)
