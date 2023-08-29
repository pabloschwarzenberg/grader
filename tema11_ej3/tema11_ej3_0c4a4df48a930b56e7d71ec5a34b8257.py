def evaluar_expresion(expresion,operandores,operandos):
    exp = list(expresion)
    if len(expresion) == 5:
      suma=0
      n1=float(exp[0])
      n2=float(exp[2])
      n3=float(exp[4])
      if exp[1] == "+":
        suma = n1 + n2
      if exp[1] == "-":
        suma = n1 - n2
      if exp[3] == "+":
        suma += n3
      if exp[3] == "-":
        suma -= n3
      return suma
     
    if len(expresion) == 6:
      suma=0
      n1=float(exp[0])
      n2=float(exp[2])
      n3=float(exp[4])*10+float(exp[5])
      if exp[1] == "+":
        suma = n1 + n2
      if exp[1] == "-":
        suma = n1 - n2
      if exp[3] == "+":
        suma += n3
      if exp[3] == "-":
        suma -= n3
      return suma
    
    if len(expresion) == 3:
      suma=0
      n1=float(exp[0])
      n2=float(exp[2])
      if exp[1] == "+":
        suma = n1 + n2
        return suma
      if exp[1] == "-":
        suma = n1 - n2
        return suma
    

if __name__=="__main__":
    print(evaluar_expresion("2+3",[],[]))
    print(evaluar_expresion("2-3",[],[]))
    print(evaluar_expresion("2+3-11",[],[]))
    print(evaluar_expresion("2-3+8",[],[]))