#Descomponer un número
numero=int(input("ingrese numero"))
def kevin(numero):
    i=4
    U=(numero//10**(i-1))%10
    return U
def kevin1(numero):
    i=3
    D=(numero//10**(i-1))%10
    return D
def kevin2(numero):
    i=2
    C=(numero//10**(i-1))%10
    return C
def kevin3(numero):
    i=1
    M=(numero//10**(i-1))%10
    return M
dg=kevin(numero)
dg1=kevin1(numero)
dg2=kevin2(numero)
dg3=kevin3(numero)
print(str (dg)+"M +" + str (dg1)+"C +" +str (dg2)+"D +"+ str (dg3)+"U")