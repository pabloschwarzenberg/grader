def divisores(numero):
    i=1
    divisores=[]
    h=numero
    while i<=numero:
        if numero%i==0:
            divisores.append(i)
            numero=numero/i
            i=i+1
            if i>numero:
                divisores.append(h)
        else:
            i=i+1
    if divisores[-2]==divisores[-1]:
       divisores.pop(-1)
    return divisores

def suma_divisores(numero):
    suma=[]
    a=0
    i=0
    while i <len(numero):
        a=a+numero[i]
        i=i+1
    return a

def comprobar(numero,numerob):
    if numero==numerob:
        print("TRUE")
        a=1
    else:
        print("FALSE")
        a=0

def buscar (numero):
    i=1
    lista=[]
    while i<numero:
        div=divisores(i)
        suma=suma_divisores(div)
        
        if suma==i:
            lista.append(i)
        i=i+1    
    if len(lista)==1:
        print("No hay numeros perfectos antes del ",numero)
    if len(lista)!=1:
        print("el numero ",lista[1]," es un numero perfecto")
    #return lista        
        

numero1=int(input("ingrese un numero: "))
div=divisores(numero1)
suma=suma_divisores(div)
comp=comprobar(suma,numero1)

nuevonumero=int(input("numero limite a buscar: "))
respuesta=buscar(nuevonumero)
print(respuesta)

           