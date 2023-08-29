hebra1=input("Hebra:")
hebra1=hebra1.upper()
i=0
c=0
while i<len(hebra1):
    if hebra1[i]=="A" or hebra1[i]=="T" or hebra1[i]=="C" or hebra1[i]=="G" :
        c=c+1
    
    if c==len(hebra1):
        print("Secuencia Correcta")
    else:
        print("Secuencia Incorrecta")
    i=i+1     