def validar_expresion(expresion):
    solucion=list(expresion)
    if "+" in solucion or "-" in solucion:
        if solucion[0]!="+" or solucion[0]!="-":
            if solucion[-1]!="+" and solucion[-1]!="-":
                if solucion.count("+")==1:
                    if solucion.count("-")==0:
                        return True
                elif solucion.count("-")==1:
                    if solucion.count("+")==0:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
        

           