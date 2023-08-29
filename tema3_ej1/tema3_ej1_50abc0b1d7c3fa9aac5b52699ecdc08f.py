# completa el código de la función
def suma_divisores(a):
    divisores = [1]
    for i in range(2, a + 1):
        if a % i == 0:
            divisores.append(i)
    return sum(divisores)
def primo (a):
    contador = 0
    resultado = True
    for p in range(1, a+1):
        if(a%p==0):
            contador+=1
        if(contador>2):
            resultado=False
            break
    return resultado
    
a = int()
if primo(a) == True:
    print("el numero es primo")
else:
    if primo(a) == False:
        print("el numero no es primo")