secadn = input("Ingrese una secuenciade ADN: ")
secadndiv = []

letras = ["a","c","t","g"] 
contador = 0
for i in (secadn):
  secadndiv.append(i.lower())
    
for i in (secadndiv):
  if i not in (letras):
    print("incorrecta")
    break
  contador += 1
    
  if (contador == len(secadn)):
    print("correcta")
    
      