def validar_expresion(e):
    i=0
    for i in range(0,len(e)):
        if e[i]=="-" and i<(len(e)-2):
            if e[i+1]=="+" or e[i+1]=="-":
                return False
            else:
                return validar_expresion(e[i+1:len(e)])
        elif e[i]=="+" and i<(len(e)-2):
            if e[i+1]=="+" or e[i+1]=="-":
                return False
            else:
                return validar_expresion(e[i+1:len(e)])
        elif e[i]=="-" and i==(len(e)-1):
            return False
        elif e[i]=="+" and i==(len(e)-1):
            return False
        elif e[i]!="-" and i==(len(e)-1):
            return True
        elif e[i]!="+" and i==(len(e)-1):
            return True

        
