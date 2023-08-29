#Factores Primos
def primo(numero):
    p = []
    
    for a in range(2, numero + 1 ):
        while numero%a ==0:
            p.append(a)
            numero = numero/a
    return p 


num = int(input("Escribe un numero entero: "))
descomposicion = (primo(num))


for item in descomposicion:
    print(item)
           