DNA=input("Ingrese tu secuencia: ")
DNA_=DNA.upper()
p=0
for i in DNA_:
    if i=="A" or i=="T" or i=="G"  or i=="C":
        p+=1
        if p==len(DNA_):
            print("secuencia correcta")
            break
    else:
        print("secuencia incorrecta")
        break
