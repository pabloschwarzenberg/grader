def genoma(string):
    pozo="BDEFHIJKLMNOPQRSUVWXYZ"
    sec="AGCT"
    for k in string:
        letras=sec.find(k)
        estar=pozo.find(k)
    if letras!=-1 and estar==-1:
        r=True
    else:
        r=False
    return r
        
        


s=input("Ingrese secuencia:")
s=s.upper()
if genoma(s):
    print("secuencia correcta")
else:
    print("secuencia incorrecta")