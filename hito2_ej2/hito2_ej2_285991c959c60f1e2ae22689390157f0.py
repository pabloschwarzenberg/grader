secuencia=input("ingrese secuencia a verificar:")
secuencia1=secuencia.lower()

i=0
while i<len(secuencia):
    secuencia_lista=list(secuencia1)
    print(secuencia_lista)
    if secuencia_lista[i]=="a" or secuencia_lista[i]=="c" or secuencia_lista[i]=="t" or secuencia_lista[i]=="g":
        i=i+1
        if len(secuencia_lista)==i:
            print("secuencia correcta")
    elif secuencia_lista[i]!="a" or secuencia_lista[i]=="c" or secuencia_lista[i]=="t" or secuencia_lista[i]=="g":
        print("secuencia incorrecta")
        break
     