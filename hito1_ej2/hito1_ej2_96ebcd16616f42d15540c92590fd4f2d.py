#Contestador de celular
"""
 Declaración de variables.
 (Termina) es una variable booleana reutilizable para terminar los bucles while.
 (comprobador) es una variable booleana que comprueba solo en el bucle donde se intruduce el número de celular.
 (numero) es la variale que guarda el número de celular como int.
 (hora) es la variable que guarda el valor de la hora en que se llama, como int.
 (cantidad_n) es una variable que guarda el número de celular pero como str para posteriormente 
              poder usarla con funciones como len() y .found(). 

"""

termina = False
comprobador = False
numero = 0
hora = 0
cantidad_n = 0


"""
 Comprobador si el input es realmente sólo números, sino, se ingresa nuevamente el número. El valor se guarda en la variable numero como int. 
 Guardar el valor de la variable numero en la variable numero_str.
 Se 
 
"""
while termina != True:
    try:
        numero = input("Número de celular del que llamas: ")
        numero_str = str(numero)
        int(numero)
        comprobador = True
    except:
        comprobador = False

    if comprobador == True:
        if len(numero_str) == 8:
            termina = True
        else:
            print("Ingresa un número de 8 cifras.\n")        
    else:
        print("Ingresa un número válido, sin letras.\n")

termina = False

while termina != True:
    hora = int(input("Hora de la llamada: "))
    if hora <= 23 and hora >= 0:
        termina = True
    else:
        print("La hora no es válida\n")

termina = False

while termina != True:

    if 0 < hora < 7:
        print("CONTESTAR.")
    elif 7 <= hora < 14 :
        if numero_str.find("909") == 5:
            print("CONTESTAR.")
        else:
            print("NO CONTESTAR.")
    elif 14 <= hora <= 17:
        print("NO CONTESTAR.")
    elif 17 <= hora < 19:
        if numero_str.find("877") == 0:
            print("NO CONTESTAR.")
        else:
            print("CONTESTAR.")
    elif 19 <= hora <= 23 :
        print("NO CONTESTAR.")        
    elif hora == 0 :
        print("NO CONTESTAR.") 
    termina = True

