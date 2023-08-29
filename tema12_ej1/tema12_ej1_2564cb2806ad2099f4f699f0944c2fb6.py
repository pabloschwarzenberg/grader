def generar(numero,largo):
  if len(numero)==largo:
    b="".join(numero)
    print(b)
    return
  for d in ["0","1"]:
    numero.append(d)
    generar(numero,largo)
    numero.pop()


#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
#print("0000")
generar([],n)