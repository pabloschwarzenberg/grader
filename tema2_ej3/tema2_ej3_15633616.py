def numero_perfecto(a):
    x=1
    y=0
    while x!=a:
        if a%x==0:
            y=y+x
        x=x+1
   
    return y==a

#esta línea sirve para que el revisor del sitio pueda importar tu programa
#y llamar a la función que creaste para verificar que funciona bien
if __name__ == "__main__":
    b=eval(input("Ingrese su numero: "))
    h=1
    j=0
    while h<b:
        if numero_perfecto(h)==True:
            j=j+h
        h=h+1
    print("La suma de los número perfectos menores a", b, "es", j)