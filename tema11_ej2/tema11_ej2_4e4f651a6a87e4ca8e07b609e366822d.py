def validar_expresion(expresion):
    
    a=0
    b=0
    for i in expresion:
        if i.isdigit()==True:
            a=a+1
        if i=="-" or i=="+":
            b=b+1
    if a==2 and b==1:
        return True
    else:
        return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           