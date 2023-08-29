import math

#MENÚ
print("______________ MENÚ ________________")
print("             Figuras:                ")
print("")
print("         1.- Triangulo")
print("         2.- Rectangulo")
print("         3.- Rombo")
print("         4.- Circulo")
print("____________________________________")

#Variable
seleccion = input("Escoja figura para calcular su area: ")

# Driver Code
if __name__=="__main__":
    main()
#Selecciones
#TRIANGULO
if seleccion > 0 and seleccion < 2:
    print("")
    print("         Area del Triangulo:")
    print("")
    base_triangulo = int(input("Digite la base del Triangulo: "))
    altura_triangulo = int(input("Digite la altura del Triangulo: "))
    area_triangulo = ((base_triangulo*altura_triangulo)/2)
    print("El area del triangulo especificado es: ",area_triangulo)
    
#RECTANGULO
if seleccion > 1 and seleccion < 3:
    print("")
    print("     Area del Rectangulo:")
    print("")
    base_rectangulo = int(input("Digite la base del Rectangulo: "))
    altura_rectangulo = int(input("Digite la altura del Triangulo: "))
    area_rectangulo = (base_rectangulo*altura_rectangulo)
    print("El area del rectangulo especificado es: ",area_rectangulo)
    
#ROMBO
if seleccion > 2 and seleccion < 4:
    print("")
    print("     Area del Rombo:")
    print("")
    diagonal_mayor = int(input("Digite el valor de la diagonal mayor: "))
    diagonal_menor = int(input("Digite el valor de la diagonal menor: "))
    area_rombo = ((diagonal_mayor*diagonal_menor)/2)
    print("El area del rombo especificado es: ",area_rombo)
    
#CIRCULO
if seleccion > 3 and seleccion < 5:
    print("")
    print("     Area del Circulo:")
    print("")
    radio_circulo = int(input("Digite el radio del circulo: "))
    area_circulo = ((math.pi)*(radio_circulo*radio_circulo))
    print("El area del circulo especificado es: ", area_circulo)