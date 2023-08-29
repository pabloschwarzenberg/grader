x=input("Ingrese palabra: ")

A=x.find("a")
C=x.find("c")
G=x.find("g")
T=x.find("t")

if A >=0 and C >=0 and G >=0 and T >=0 and len(x)<4:
    print("secuencia correcta")

else :
    print("secuencia incorrecta")