# Un número se dice número perfecto 
# si la suma de todos sus divisores es igual al mismo número (No debes considerar como divisor al mismo número).
# Crea una función llamada a_perfecto que reciba un número y
# retorne True si es un número perfecto
# retorne False en caso de no serlo

def numero_perfecto(numero):
    suma=0
    for i in range(1,numero):
        print(i, numero%i)
        if numero%i==0:
            suma=suma+i
    if suma==numero:
        return True
    else:
        return False

if __name__=="__main__":
    numero=int(input("Ingrese a: "))
    print(numero_perfecto(numero))