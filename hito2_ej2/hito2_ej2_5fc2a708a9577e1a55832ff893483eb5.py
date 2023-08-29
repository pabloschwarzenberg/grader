n=input("Ingrese secuencia de ADN: ")
n = n.upper()
a=[]
b=0
secuencia_adn={"A","C","T","G"}
for i in n:
    a.append(i)
for i in a:
    if not i in secuencia_adn:
        print("secuencia incorrecta")
        b=1
        break
if b==0:
    print("secuencia correcta")