def jerigonzo(palabra):
  vocales=list("aeiou")
  jerigonzo=[]
  for i in range(len(palabra)):
    jerigonzo.append(palabra[i])
    if palabra[i] in vocales:
      jerigonzo.append("p")
      jerigonzo.append(palabra[i])
  jerigonzo="".join(jerigonzo)
  return jerigonzo

    
         