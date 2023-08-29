print ("rectangulo")
print ("triangulo")
print ("rombo")
print ("circulo")

figura = input("de que figura desea calcular el area: ")

if figura == "rectangulo":
  base = int(input("ingrese base: "))
  altura = int(input("ingrese altura: "))
  area = base * altura 
  print("area rectangulo: ",area)
elif figura == "triangulo":
  base = int(input("ingrese base: "))
  altura = int(input("ingrese altura: "))
  area = (base * altura)/2
  print("area triangulo: ",area)
elif figura == "rombo":
  diagonal_1 = int(input("ingrese diagonal 1: "))
  diagonal_2 = int(input("ingrese diagonal 2: "))
  area = (diagonal_1 * diagonal_2)/2
  print("area rombo: ",area)
elif figura == "circulo":
  radio = int(input("ingrese radio: "))
  area = 3.1416 * radio**2
  print ("area circulo: ",area)