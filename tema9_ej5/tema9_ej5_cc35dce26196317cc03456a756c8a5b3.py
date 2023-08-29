Animal = ["Perro", "Gato", "Gallina", "Oveja", "Vaca", "Cerdo"]
Nombre = ["Piggy", "Nerón", "Margarita", "Manchitas", "Mimun", "Carlota"]
combi_list = []

for i in range(0, len(Animal)):
    z = random.choice(Animal)
    o = random.choice(Nombre)
    combi_list.append([z,o])
    Animal.remove(z)
    Nombre.remove(o)
print(combi_list)


print("")
print("")
print("")


print("Seleccione a continuacion una opcion: \n")


print("Opcion 1: Indicar la posición dentro de la lista combinada de un nombre. En el ejemplo, al ingresar 'Carlota', debiera responder posición=7 \n")
print("Opción 2: Indicar el tipo de mascota que tiene el nombre con más letras. En el ejemplo es 'Gallina' \n")
print("Opción 3: Indicar el tipo de mascota a partir de su nombre. Ej. con el valor 'Margarita', la respuesta debiera ser: Margarita es un(a) Gallina \n")
print("Opción 0: El programa sale del menú y finaliza \n")



print("______________________________________________________")
selec = int(input("Opcion: "))

while selec >= 0 and selec <= 3:
  if selec == 0 :
    selec = - 1
    print("Hasta la proxima :D ")
    break

    
  elif selec == 1 :
    print("Ingrese el nombre para saber su posición")
    posicion = input()
    for f in range(6):
      if (combi_list[f][1]) == str(posicion):
        e = str(combi_list[f][0])
        g = [e, str(posicion)]
        posicion2 = combi_list.index(g)
        posicion2 += 1
        print(posicion2)
        selec = -2

  elif selec == 2:
    for f in range (6):
      if len(combi_list[f][1])==9:
        print(combi_list[f][0])
        selec = -3

  elif selec ==3:
    print("Nombre de mascota: ")
    buscar = input()
    for f in range(6):
      if (combi_list[f][1]) == str(buscar):
        a = str(combi_list[f][0])
         print(buscar, f"es un(a) {a}")
         selec = -4
    
         