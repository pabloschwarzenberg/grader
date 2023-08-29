def validar_expresion(expresion):
    lista=["+","-"]
    for i in expresion:
      if i in lista:
        if i[[i]+1] in lista:
          return False
        else:
          break  
    return True


if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           