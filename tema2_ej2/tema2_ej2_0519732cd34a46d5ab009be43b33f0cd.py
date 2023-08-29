# completa el código de la función
def amigos(a,b):
    a= int(input("Ingrese un numero: "))
    b= int(input("Ingrese un numero: "))
    x= 1
    suma= 0
    while x<a:
        if a % x == 0:
            suma= suma+x
        x= x+1
    if suma ==b:
       print("Los numeros son amigos")
    else:
       print("No son amigos")