def validar_expresion(expresion):
     if len(expresion) == 3:
         if expresion[0].isdigit() == True and expresion[2].isdigit() == True:
            if expresion[1] in ["+", "-"]:
                return True
     return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           