#Contestador de celular
nt=input("Ingrese numero telefonico: ")
lista=[]
for i in nt:
    lista.append(int(i))

while len(lista)!=8:
    lista=[]
    nt=input("Ingrese numero telefonico, nuevamente: ")
    for i in nt:
        lista.append(int(i))

hl=int(input("Ingrese hora de la llamada: "))

a=lista[0]
b=lista[1]
c=lista[3]
e=lista[5]
d=lista[6]
f=lista[7]

resultado=str()

if hl>0 and hl<7:
    resultado=str("CONTESTAR")
    print("Resultado: ", resultado)

elif hl<14 and hl>7:
    if e==9 and d==0 and f==9:
        resultado=str("CONTESTAR")
        print("Resultado: ", resultado)
    else:
        resultado=str("NO CONTESTAR")
        print("Resultado: ", resultado)

elif hl>17 and hl<19:
    if a==8 and b==7 and c==7:
        resultado=str("CONTESTAR")
        print("Resultado: ", resultado)
    else:
        resultado=str("NO CONTESTAR")
        print("Resultado: ", resultado)

else:
    resultado=str("NO CONTESTAR")
    print("Resultado: ", resultado)  