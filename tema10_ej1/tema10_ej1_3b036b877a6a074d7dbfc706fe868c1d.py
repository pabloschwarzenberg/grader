def mcm(a,b,ab):
 def mcd(a,b):
    if a>b:
        dividendo=a
        divisor=b
        cociente=(a//b)
        resto=a%b
    elif b>a:
        dividendo=b
        divisor=a
        cociente=(b//a)
        resto=b%a
    dividendo=divisor*cociente+resto
    print(dividendo,"=",divisor,cociente,"+",resto)
    if resto==0:
        return divisor
    else:
        return mcd(divisor,resto)
 resultado=ab/mcd(a,b)
 return resultado

if __name__=="__main__":
    pass
           