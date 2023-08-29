      #validar secuencia
secuencia=input("Secuencia: ").upper()
genoma=["A","C","T","G"]
suma=0
for i in secuencia:
    if not i in genoma:
        suma+=1
if suma==0:
    print("secuencia correcta")
else:
    print("secuencia incorrecta")
        
