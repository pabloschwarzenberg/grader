def mcd(a,b):
    if b==0:
        return a
    parte_ent=a//b
    resto=a-b*parte_ent
    return mcd(b,resto)
def mcm(a,b,c):
    h=int(mcd(a,b))
    resultado=c/h
    return resultado
 

 