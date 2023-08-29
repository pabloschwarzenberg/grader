def validar_expresion(expresion):
    g = expresion
    patron = "+"
    patron2 = "-"
    algo = True
    partida = 0
    contar=0
    while algo:
        a = g.find(patron, partida)
        b = g.find(patron2, partida)
        if a != -1:
            contar+=1
            partida+=a+1
        elif b!=-1:
            contar+=1
            partida+=b+1
        else:
            algo=False

    if len(expresion)==3 and contar==1:
        if expresion[1]=="+" or expresion[1]=="-":
            expresion = list(expresion)
            expresion[0] = int(expresion[0])
            expresion[2] = int(expresion[2])
            if type(expresion[0])==int and type(expresion[2]==int):
                return True
            else:
                return False
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
           