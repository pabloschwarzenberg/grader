print("Desea jugar con palabras de que son marcas de coches o nombres de paises")
time.sleep(2)
 
cat_seleccionada = input("Ingrese C para marcas de coches y P para nombres de paises: ")
 
while True:
    if cat_seleccionada.lower() == "c":
        print("excelente a seleccionado marcas de coches")
        palabra_secreta = random.choice(marcas_de_coches)
        break
    elif cat_seleccionada.lower() == "p":
        print("excelente a seleccionado nombres de paises")
        palabra_secreta = random.choice(nombres_de_paises)
        break
 
    else:
        print("Por favor seleccione una categoria valida")
        cat_seleccionada = input("Ingrese C para marcas de coches y P para nombres de paises: ")