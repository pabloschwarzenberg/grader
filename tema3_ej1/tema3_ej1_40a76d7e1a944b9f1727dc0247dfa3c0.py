"""
Crea una función que calcule la suma de los divisores de un número sin incluir al número,llamada suma_divisores. 
Junto con la suma de los divisores haz que la función regrese si el número es primo o no, 
intensamente que si la suma de sus divisores es 1, el número es primo.

Importante: en este ejercicio solamente debes entregar funciones 
(que reciben los parámetros indicados en el ejercicio y que entregan su resultado con return), 
los input y los print para probar tu función los debes poner dentro de un 
if __name__ == "__main__": o quitarlos del programa al momento de subirlo a la plataforma.

completa el código de la función
"""
    
def suma_divisores(numero):
    suma=0
    for i in range(1,numero):
        print(i, numero%i)
        if numero%i==0:
            suma=suma+i
    if suma==1:
        return suma,True
    else:
        return suma,False
    
#esta linea sirve para que el revisor del sitio pueda importar tu programa
#y llamar a la funcion que creaste para verificar que funciona bien
if __name__ == "__main__": #lo exige la pagina de hitos
    numero=int(input("Ingrese su numero: "))
    suma,vf=suma_divisores(numero)
    print("la suma del divisor es: ",suma,vf)
    