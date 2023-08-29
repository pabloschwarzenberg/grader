def validar_expresion(ex):
    num="1234567890"
    ope=("+","-")
    if len(ex)==1 and ex in num:
        return True
    if len(ex)==2 and ex[0] in ope and ex[1] in num:
        return True
    if len(ex[-2:])>=2 and ex[-2:][0] in ope and ex[-2:][1] in num:
        return validar_expresion(ex[:-2])
    return False
#print(validar_expresion("2+3"))
#print(validar_expresion("2-3"))
#print(validar_expresion("2++"))
#print(validar_expresion("--2"))
#print(validar_expresion("2-"))
#print(validar_expresion("2+6+7+9+8+7-6-9"))
#print(validar_expresion("2+6+7+9+8++7-6-9"))
#print(validar_expresion("4+6+5+4+8++"))
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           