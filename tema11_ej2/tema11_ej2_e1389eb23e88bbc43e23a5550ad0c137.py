def validar_expresion(expresion):
    signos = "+","-"
    if len(expresion) == 1:
      if expresion.isnumeric():
        return True
      else:
        return False
    else:
      for i in range(len(expresion)):
        elemento=expresion[i]
        if elemento in signos:
          if i==len(expresion)-1:
            return False
          else:
            numero=expresion[:i]
            resto=expresion[i+1:]
      if numero.isnumeric():
        return validar_expresion(resto)
      else:
        return False
    
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           