def ver_lista():
  print(lista_articulos)
  print()
  print("Articulos en tu lista")
  print("------------")
  for articulos in lista_articulos:
    print("------------")
    print(articulos)
    print("------------")
  print("------------")
  print("Estos son tus articulos")
  print()
 
 
while  True:
	try:
		print("Menú")
		print ("1.- Agregar artículos")
		print ("2.- Borrar artículos")
		print ("3.- Ver lista de artículos")
		print ("4.- Salir")
 
p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
      
    print("Favor de ingresar una opcion valida")
  else:
		#si no es ninguna de las 4 opciones validas
		if opcion < 0 or opcion >4:
				print ("no es una opcion valida")
				continue
		if opcion == 1:
			agregar_articulos()
		elif opcion == 2:
			borrar_articulos()
		elif opcion == 3:
			ver_lista()
		else:
			break
print("Gracias por utilizar la lista hecha en Python")
