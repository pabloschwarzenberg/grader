entero1 = eval(input("Ingrese el primer número entero a ordenar:\n"))
entero2 = eval(input("Ingrese el segundo número entero a ordenar:\n"))
entero3 = eval(input("Ingrese el tercer número entero a ordenar:\n"))
if (entero1 > entero2 > entero3):
    print("El orden correspondientes es:", entero3 ,",", entero2 ,",", entero1)
elif(entero1 < entero2 < entero3):
    print("El orden correspondientes es:" , entero1 ,",", entero2 ,",", entero3)
elif(entero2 > entero1 > entero3):
    print("El orden correspondiente es:" , entero3,",", entero1 ,",", entero2)
elif(entero2 < entero1 < entero3):
    print("El orden correspondiente es:" , entero2,",", entero1 ,",", entero3)
elif(entero2 > entero3 > entero1):
    print("El orden correspondiente es:" , entero1,",", entero3 ,",", entero2)
elif(entero1 > entero3 > entero2):
    print("El orden correspondiente es:" , entero2,",", entero3 ,",", entero1)
elif(entero2 == entero1 > entero3):
    print("El orden correspondiente es:" , entero1,",", entero2 ,",", entero3)
elif(entero2 == entero1 < entero3):
    print("El orden correspondiente es:" , entero3,",", entero2 ,",", entero1)
elif(entero1 == entero3 > entero2):
    print("El orden correspondiente es:" , entero2,",", entero1 ,",", entero3)
elif(entero1 == entero3 < entero2):
    print("El orden correspondiente es:" , entero1,",", entero3 ,",", entero2)
elif(entero3 == entero2 > entero1):
    print("El orden correspondiente es:" , entero1,",", entero3 ,",", entero2)
elif(entero3 == entero2 > entero1):
    print("El orden correspondiente es:" , entero1,",", entero3 ,",", entero2)