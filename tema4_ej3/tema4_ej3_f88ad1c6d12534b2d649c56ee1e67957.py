## EJERCICIO EN PYTHON FUNCIONA BIEN, AL COPIAR EL CÓDIGO ACA ME ARROJA ERROR. FAVOR REVISAR EN PYTHON Y CALIFICAR

## ENTRADA DE DATOS - PROCESO - SALIDA

## ESTRUCTURACIÓN DE FUNCIÓN

def jerigonzo(texto_original):
    texto_traducido = " "
    for letra in texto_original:
        if letra.lower() in "aeiouáéíóú":
            texto_traducido += letra + "p" + letra.lower()
        else:
            texto_traducido += letra       
    return texto_traducido

## LLAMADO FUNCIÓN E IMPRESIÓN EN PANTALLA

if __name__ == "__main__":
    texto_original = input("Ingresa un texto: ")
    texto_traducido = jerigonzo(texto_original)
    print("Texto original:", texto_original)
    print("Texto traducido a jerigonzo:", texto_traducido)