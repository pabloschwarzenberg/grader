def validar_expresion(expresion):
    if expresion.isdigit()==True:
      return True
    
    lista1=[]
    lista2=[]
    for i in range(len(expresion)):
      if expresion[i] == "+" or expresion[i]== "-":
        lista1= expresion[:i]
        lista2 = expresion[i+1:]
        if validar_expresion(lista1) == True and validar_expresion(lista2)==True:
          return True
        break
    return False
    
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           