p1=input("ingrese ADN:  ")
p1=p1.upper()
i=0
while i<len(p1):
    print(p1[i])
    if p1[i]==("A")or p1[i]==("C")or p1[i]==("T")or p1[i]==("G"):
        print("secuencia correcta")
    else:
        print("secuencia incorrecta")
    i=i+1