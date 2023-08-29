def validar_expresion(expresion):
    carac=["+","-"]
    numeros=["0","1","2","3","4","5","6","7","8","9"]
    if len (expresion)<3:
       return False
    if len (expresion)==3:
      if expresion[0] in numeros and expresion[1] in carac and expresion[2] in numeros:
        return True
      else:
        return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           