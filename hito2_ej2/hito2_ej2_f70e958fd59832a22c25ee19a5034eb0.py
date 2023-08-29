palabra=input("Ingrese palabra: ")
palabra.lower()
i=0
c=True
while(i<len(palabra)and c==True):
    if(palabra[i]=='a' or palabra[i]=='c' or palabra[i]=='g' or palabra[i]=='t'):
        print(palabra[i])
    else:
        print("Secuencia incorrecta")
        c=False
    i=i+1
if(c==True):
    print("Secuencia correcta")
