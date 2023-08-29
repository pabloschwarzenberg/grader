def interpretar(expresion):
  expresion=list(expresion)
  if len(expresion)==3:
    x1=float(expresion[0])
    x2=float(expresion[2])
    if expresion[1]=="*":
      resultado=x1 * x2
      return str(resultado)
    elif expresion[1]=="/":
      resultado=x1 / x2
      return str(resultado)
    elif expresion[1]=="+":
      resultado= x1 + x2
      return str(resultado)
    else:
      resultado= x1 - x2
      return str(resultado)
  else:
    contador1 = -1
    contador2=-1
    while contador1<=len(expresion):
        for i in expresion:
            contador1+=1
            if i=="*" or i=="/":
                resultado=interpretar(expresion[contador1-1:contador1+2])
                expresion.pop(contador1)
                expresion.pop(contador1 )
                expresion.pop(contador1-1)
                expresion.insert(contador1-1,resultado)
                contador1=-1
                break
            else:
                continue
    while contador2<=len(expresion):
        for j in expresion:
          contador2+=1
          if j=="+" or j=="-":
              resultado = interpretar(expresion[contador2 - 1:contador2 + 2])
              expresion.pop(contador2)
              expresion.pop(contador2)
              expresion.pop(contador2 - 1)
              expresion.insert(contador2 - 1, resultado)
              contador2 = -1
              break
          else:
            continue

    return float(expresion[0])
      
  

resultado=interpretar("2*3+5+6*7/9")
print(resultado)
#el resultado debiera ser 15.66666
      