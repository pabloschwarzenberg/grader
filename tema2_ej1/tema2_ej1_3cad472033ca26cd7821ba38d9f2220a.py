while True:
  print("**Menú Principal**")
  print("1.- Calcular el área de un triángulo.")
  print("2.- Calcular el área de un rectángulo. ")
  print("3.- Calcular el área de un rombo. ")
  print("4.- Calcular el área de un círculo. ")
opcion = int(input("Ingrese el numero de la opcion que desea calcular: "))
  
if opcion==1:
    def area_triangulo(base,altura):
      areatrian=(base*altura)/2 #Fórmula del área de un triángulo.
      return areatrian

#Ingreso de datos por usuario.
    base=float(input("Ingrese el valor de la base del triángulo: "))
    altura=float(input("Ingrese el valor de la altura del triángulo: "))

#Resultado.
    resultado=area_triangulo(base, altura)
    print("El área del triángulo es igual a: ", {resultado})
    

elif opcion==2:
    def area_rectangulo(base,altura):
      arearect=base*altura  #Fórmula del área de un rectángulo
      return arearect

#Ingreso de datos por usuario.
    base=float(input("Ingrese valor del ancho de rectángulo: "))
    altura=float(input("Ingrese valor del largo de rectángulo: "))

#Resultado.
    resultadorect=area_rectangulo(base, altura)
    print("EL área del rectángulo es igual a: ", {resultadorect})

elif opcion==3:
    def area_rombo(diagonal1,diagonal2):
      arearomb=(diagonal1*diagonal2)/2 #Fórmula del área de un rombo.
      return arearomb

#Ingreso de datos por usuario.
    diagonal1=float(input("Ingrese el valor de la primera diagonal: "))
    diagonal2=float(input("Ingrese el valor de la segunda diagonal: "))

#Resultado.
    resultadoromb=area_rombo(diagonal1, diagonal2)
    print("El área del rombo es igual a: ", {resultadoromb})

elif opcion==4:
    def area_circulo(radio):
      import math
      areacirc=math.pi*(radio*radio)  #Fórmula del área de un círculo.
      return areacirc

#Ingreso de datos por usuario.
    radio=float(input("Ingrese el radio del círculo: "))

#Resultado.
    resultadocirc=area_circulo(radio)
    print("El área del círculo es igual a: ", {resultadocirc})

else:
      print("Digite nuevamente la opción que desea.")
