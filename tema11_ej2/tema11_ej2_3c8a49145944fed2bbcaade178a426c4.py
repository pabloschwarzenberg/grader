def validar_expresion(expresion):
    l=[]
    for letra in expresion:
        l.append(letra)

    if (l[0]=="1" or l[0]=="2" or l[0]=="3" or l[0]=="4" or l[0]=="5" or l[0]=="6" or l[0]=="7" or l[0]=="8" or l[0]=="9") and (l[-1]=="1" or l[-1]=="2" or l[-1]=="3" or l[-1]=="4" or l[-1]=="5" or l[-1]=="6" or l[-1]=="7" or l[-1]=="8" or l[-1]=="9" or l[-1]=="0"):
        return True

    if l[-1]!="1" or l[-1]!="2" or l[-1]!="3" or l[-1]!="4" or l[-1]!="5" or l[-1]!="6" or l[-1]!="7" or l[-1]!="8" or l[-1]!="9" or l[-1]!="0":
        return False

    if l[0]=="+" or l[0]=="-":
        return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           