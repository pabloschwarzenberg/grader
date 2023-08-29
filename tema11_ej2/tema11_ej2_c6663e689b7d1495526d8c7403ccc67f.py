def validar_expresion(exp,d=[],op=[]):
    if exp=="":
        if len(d)>len(op):
            return True
        else:
            return False
    else:
        if exp[0].isdigit():
            cont=0
            try:
                while exp[cont].isdigit():
                    cont+=1
            except IndexError:
                pass
            dcop=d.copy()
            cop=op.copy()
            dcop.append(exp[:cont])
            nueva=exp[cont:]
            return validar_expresion(nueva,dcop,cop)
            
        else:
            dcop=d.copy()
            cop=op.copy()
            cop.append(exp[0])
            nueva=exp[1:]
            return validar_expresion(nueva,dcop,cop)

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           