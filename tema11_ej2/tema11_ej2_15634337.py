__author__ = 'Domingo'
def validar_expresion(expresion):
    lista=[]
    l=len(expresion)
    num=['0','1','2','3','4','5','6','7','8','9']
    sim=['+','-']
    for i in expresion:
        lista.append(i)
    if l==0:
        return False
    empieza_con_signo=lista[0] in sim
    if empieza_con_signo==True:
        return False
    if l !=1 and l!=0:
        for i in range(len(expresion)):
            numerico=lista[i] in num
            simbolico= lista[i] in sim
            if numerico==True:
                pass
            elif simbolico==True:
                for j in range(i+1):
                    lista.pop(0)
                break
            else:
                return False
        nueva=''.join(lista)
        return validar_expresion(nueva)
    elif l==1:
        sera_num=lista[0] in num
        if sera_num==True:
            return True
        else:
            return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           