import math
def validar_expresion(expresion):
    list=[]
    for i in expresion:
        list.append(i)
    for t in list:
        if t == "+" or "-":
            if list[list.index(t)+1] == "+" or "-":
                return False
            else:
                return True
            
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))