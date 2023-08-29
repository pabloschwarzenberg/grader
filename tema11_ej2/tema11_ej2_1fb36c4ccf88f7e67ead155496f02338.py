operadores = ["+","-"]
numeros = ["1","2","3","4","5","6","7","8","9","0"]
def validar_expresion(expresion, strout = ""):

    current = expresion[1:]
    pred = expresion[0]
 

    if len(current) > 0:
        if (current[0] in operadores and pred in numeros and len(expresion)%2 != 0) or (current[0] in numeros and pred in operadores and len(expresion)%2 == 0):
            
            return validar_expresion(current)
       
        else:
            return False
    
    return True
if __name__=="__main__":
    print(validar_expresion("2+3+7"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
