s=input("Ingrese un posible codigo genetico: ")
s=s.upper()
i=0
largo=len(s)
valido=True
while largo>i:
    if s[i]=="C" or s[i]=="G" or s[i]=="A" or s[i]=="T":
        i=i+1
        continue
    else:
        valido=False
        break
if valido==True:       
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")    
    