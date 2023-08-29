#Factores Primos
def es_primo(numero, n=2):
    if numero == 0 or numero == 1 or numero == 4:
        return False
    # para sacar los multiplos
    for x in range(2, int(numero/2)):
        if numero % x == 0:
            return False
    return True 

numero=int(input("Porfavor ingrese un numero: "))
es_primo(numero)
#numeros amigos
def amigos(a,b):
    suma_a=0
    suma_b=0
    for i in range(1,a):
        if a%i==0:
            suma_a+=i
 
    for x in range(1,b):
        if b%x==0:
            suma_b+=x
 
    return suma_a==b and suma_b==a