# completa el código de la función
def amigos(a,b):
    x=1
    suma=0
    while x < a:
        if a % x== 0:
            suma = suma + x
        x = x + 1
    if suma == b:
        numeroamigo=bool(1)
        # numeroamigo=print("True")
    else:
        numeroamigo=bool(0)
        # numeroamigo=print("False")
    return(numeroamigo)
try:
    numero1=int(input("Ingrese un numero 1:\n"))
    numero2=int(input("Ingrese un numero 2:\n"))
	
    print(amigos(numero1,numero2))	
except EOFError as e:
	print(e)
