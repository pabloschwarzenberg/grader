# completa el código de la función
def suma_divisores(a):
    divisores=[]
    contador=0
    resultado=True
    for i in range(1,a):
        if a% i==0:
           divisores.append(i)
    suma=sum(divisores)
    
    if suma>1 or a==1:
       resultado=False
    if suma==1:
       resultado=True
    return (suma,resultado)
if __name__ == "__main__":
    numero=eval(input("Ingrese su numero: "))
    respuesta=suma_divisores(numero)
    print("La suma de los divisores de",numero,"es:",respuesta)
    
   
