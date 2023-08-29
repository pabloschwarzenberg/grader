# por favor escribe aquí tu función
numero = (input("ingrese un número: ")))
def es_primo(numero):
    contador = 0
    for i in range(2,numero):

        if (numero < 2):
            return False
        if ((numero % i) == 0):
            return False
        return True
          
print(es_primo(n))