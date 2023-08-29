sec=["A","C","T","G"]
ent=list(input("Ingrese secuencia: "))

p=0
for i_sec in sec:
    for i_ent in ent:
        if(i_sec==i_ent.upper()):
            p=p+1
   
if(p==len(ent)):
    print("secuencia correcta")
else:
    print("secuencia incorrecta")    