# por favor escribe aquí tu función
def es_primo(num, n=2):
    if (n >= num):
        print("Es primo")
        return True
    elif (num % n != 0):
        return es_primo(num, n+1)
    else:
        print("No es primo")
        return False
num = int(input("Porfavor ingrese un numero: "))
es_primo(num)