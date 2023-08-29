def validar_expresion(expresion):
    elementos=["+","-"]
    numeros=["1","2","3","4","5","6","7","8","9","0"]
    if expresion[0] in numeros and expresion[len(expresion)-1] in numeros:
      if len(expresion)==3:
        return(True)
      else:
        return(validar_expresion(expresion[2:len(expresion)-3]))
    if expresion[0] not in numeros or expresion[len(expresion)-1] not in numeros:
        return (False)

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           