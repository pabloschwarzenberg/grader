def validar_expresion(expresion):
    if len(expresion)==3:
      numeros=["0","1","2","3","4","5","6","7","8","9"]
      if (expresion[0] in numeros and expresion[2] in numeros) and (expresion[1]=="+" or expresion[1]=="-"):
        return True
      else:
        return False
    else:
      return False 

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           