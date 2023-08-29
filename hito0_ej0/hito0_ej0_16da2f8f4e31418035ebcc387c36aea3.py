#Lo siento, no se me ocurrio como marcar cuando habia mas de un numero, o sea en ves de un 2, 
#que hay un 22 o algo asi, como pueden ver me complique demasiado :c
#¿Hay alguna forma de saber como pudo haber sido el codigo en esta parte?
def interpretar(expresion):
    if expresion.find("+")==-1 and expresion.find("-")==-1 and expresion.find("*")==-1 and expresion.find("/")==-1:
        return expresion
    if expresion.find("/")!=-1 and (expresion.find("*")>expresion.find("/") or expresion.find("*")==-1):
        r=int(expresion[expresion.find("/")-2:expresion.find("/")])/int(expresion[expresion.find("/")+1])
        if expresion.find("/")==1:
            return interpretar(str(r)+expresion[3:])
        if expresion.find("/")==len(expresion)-2:
            return interpretar(expresion[0:len(expresion)-4]+str(r))
        else:
            return interpretar(expresion[0:expresion.find("/")-1]+str(r)+expresion[expresion.find("/")+2:])
    if expresion.find("*")!=-1 and (expresion.find("/")>expresion.find("*") or expresion.find("/")==-1):
        r=int(expresion[expresion.find("*")-1])*int(expresion[expresion.find("*")+1])
        if expresion.find("*")==1:
            return interpretar(str(r)+expresion[3:])
        if expresion.find("*")==len(expresion)-2:           
            return interpretar(expresion[0:len(expresion)-3]+str(r))
        else:
            return interpretar(expresion[0:expresion.find("*")-1]+str(r)+expresion[expresion.find("*")+2:])
    if expresion.find("+")!=-1:
        r=int(expresion[expresion.find("+")-1])+int(expresion[expresion.find("+")+1])
        if expresion.find("+")==1:
            return interpretar(str(r)+expresion[3:])
        if expresion.find("+")==len(expresion)-2:
            return interpretar(expresion[0:len(expresion)-3]+str(r))
        else:
            return interpretar(expresion[0:expresion.find("+")-1]+str(r)+expresion[expresion.find("+")+2:])
    if expresion.find("-")!=-1:
        r=int(expresion[expresion.find("-")-1])-int(expresion[expresion.find("-")+1])
        if expresion.find("-")==1:
            return interpretar(str(r)+expresion[3:])
        if expresion.find("-")==len(expresion)-2:
            return interpretar(expresion[0:len(expresion)-3]+str(r))
        else:
            return interpretar(expresion[0:expresion.find("-")-1]+str(r)+expresion[expresion.find("-")+2:])

resultado=interpretar("2*3+5+6*7/9")
print(resultado)
#el resultado debiera ser 15.66666
      