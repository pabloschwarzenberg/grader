#Programa para ordenar numeros de menor a mayor
numero_uno= int(input(" introduzca un numero : "))
numero_dos= int(input(" introduzca un segundo numero : "))
numero_tres= int(input(" introduzca un tercer numero : "))
if numero_uno <= numero_dos <= numero_tres:
    print("El orden de menor a mayor seria:" ,numero_uno,",",numero_dos,",",numero_tres)
if numero_uno <= numero_tres <= numero_dos:
    print("El orden de menor a mayor seria:" ,numero_uno,",",numero_tres,",",numero_dos)


elif numero_tres <= numero_dos <= numero_uno:
    print("El orden de menor a mayor seria:" ,numero_tres,",",numero_dos,",",numero_uno)
elif numero_tres <= numero_uno <= numero_dos:
    print("El orden de menor a mayor seria:" ,numero_tres,",",numero_uno,",",numero_dos)
       

elif numero_dos <= numero_uno <= numero_tres:
    print("El orden de menor a mayor seria:" ,numero_dos,",",numero_uno,",",numero_tres)
elif numero_dos <= numero_tres <= numero_uno:
    print("El orden de menor a mayor seria:" ,numero_dos,",",numero_tres,",",numero_uno)
       
print(" Fin.")    
    

