b=""
def Genoma(b):
    b = input()
    c = b.upper()
    d = list(c)
    for i in d:
        print(i)
        if i=="A":
            d.remove("A")
        elif i=="G":
            d.remove("G")
        elif i=="T":
            d.remove("T")
        elif i=="C":
            d.remove("C")
    print(d)
    if len(d)==0:
        return True
    else:
        return False
if Genoma(b)==True:
    print("secuencia correcta")
else:
    print("secuencia incorrecta")