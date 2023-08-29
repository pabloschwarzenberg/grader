def decodificar(mensaje):
   opcion = ""
   letra = ""
   numero = ""
   if (opcion == 1):
        letra=input("\nIntroduce la Letra > ")
        ord(letra) #Con esto lo que hago es que muestre el valor ascii de la variable
        letra2 = ord(letra) #Copio el valor a otra variable
        print("El valor Ascii es:",  +letra2)
        print("\n\n")
   elif (opcion == 2):
        numero=input("\nIntroduce el numero > ")
        chr(numero) #Valor que me da
        numero2 = chr(numero) #copio el valor a otra variable
        print("\nEl valor de la letra es:", +numero2)
        print("\n\n")
 
   else:
        print("No valido")
        print("\n\n")

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         