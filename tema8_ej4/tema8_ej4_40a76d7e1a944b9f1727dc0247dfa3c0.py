"""
El encriptador ROT13 , es un tipo de llamador de desplazamiento. 
Este tipo de grabadores eran usados en tiempos de los romanos para proteger mensajes militares importantes. 
Se dice que Julio César, usaba este tipo de algoritmo para proteger sus mensajes, razón por la cual, 
se le suele llamar “cifrado César” a este tipo de codificación. 
Crea la función rot13 que recibe una palabra y la respuesta encriptada.
"""

espanol="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
codigo= "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"

def rot13(palabra):
    indice_palabra= 0
    for i in palabra:
        print(i)   
        print(indice_palabra)
        
        indice_espanol=espanol.find(i)
        print(indice_espanol)
        
        codigo_letra=codigo[indice_espanol]
        print(codigo_letra)
        
        #palabra=palabra.replace(palabra[indice_palabra],codigo[indice_español])
        palabra=list(palabra)
        palabra[indice_palabra]=codigo[indice_espanol]
        palabra="".join(palabra)
        indice_palabra=indice_palabra+1
    
    return palabra

    
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)