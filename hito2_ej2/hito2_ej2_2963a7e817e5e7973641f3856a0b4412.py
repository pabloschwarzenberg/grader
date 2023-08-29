genoma=input()
genoma_valido=["A","C","T","G","a","c","t","g"]
i=0
while i<=len(genoma)-1:
    if genoma[i] not in genoma_valido:
        print("secuencia incorrecta")
        break
    i+=1
    if i==len(genoma):
        print("secuencia correcta")      