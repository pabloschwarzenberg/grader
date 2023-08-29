#Descomponer un número
      op = "s"
while (op == "S" or op == "s"):
    #Entrada
    numero = int(input('Ingrese un número de 4 cifras: '))
    #Proceso se basa en divisiones y restos sucesivas entre 10
    auxiliar = numero
    Unidades = auxiliar%10  #Resto
    auxiliar = auxiliar//10 #Cociente entero
    Decenas = auxiliar%10
    auxiliar = auxiliar//10
    Centenas = auxiliar%10
    auxiliar = auxiliar//10
    Miles =  auxiliar%10
    auxiliar = auxiliar//10
    #Salidas
    print('Descomposición de ',numero,':'Miles'M + 'Centenas'C + 'Decenas'D + 'Unidades'U' 
    op = input('¿Realizar otra operación? (S/N): ')
print('Proceso finalizado...')