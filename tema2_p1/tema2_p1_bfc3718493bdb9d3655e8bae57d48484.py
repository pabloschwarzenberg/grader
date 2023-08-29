# por favor escribe aquí tu función
n=int(input("ingrese un numero: "))
def evaluar_primo(n):
    contador=0
    resultado=True
    for i in range(1,n+1):
        if (n%i==0):
            contador+=1
        if (contador>2):
            resultado=False
            break
     return resultado
 if (evaluar_primo(n)==True):
     print("el numero es primo")       
 else:
     print("el numero no es primo")