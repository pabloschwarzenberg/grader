import os
import time
import random
# Declaración de funciones
# Genera los valores en la matriz
def genera_matriz(m,o):
    print ("Ingrese los valores para generación de números")
    v1 = int(input("Ingrese el primer valor entero: "))
    v2 = int(input("Ingrese el segundo valor entero: "))
    print ("\nGenerando datos de la matriz...")
    for i in range(o):
        m.append([]) #Agregamos una fila vacía
        for j in range(o):
            valor = random.randint(v1,v2)
            m[i].append(valor)
    print ("Matriz de números enteros generada!!!")
    ct = input("Presione cualquier tecla para continuar...")

# Muestra los valores de la matriz guardados en la lista anidada
def mostrar_matriz(m,o): # expone los valores de la matriz
    print ("\nDatos de la matriz guardada en memoria principal\n")
    for i in range(o): 
        for j in range(o):
            print(m[i][j],"\t",end="")
        print()

# Guarda los valores de la matriz en un archivo de texto
def guardar_mat_archivo(m,o):
    nfa = "matriz_cuadrada_"+str(o)+"x"+str(o)+".txt"
    f = open(nfa,"w")
    print("\nGuardando datos de la matriz en archivo")
    for i in range(o):
        cad = ""
        for j in range(o):
            cad = cad + str(m[i][j]) + "\t"
        cad.rstrip("\t")
        cad = cad +"\n"
        f.write(cad)
    f.close()
    print ("Matriz guardada en archivo!!!")

# Lee del archivo los datos de la matriz y los muestra por pantalla
def recuperar_mat_archivo(o):
    print("\nDatos de la matriz recuperada del archivo")
    nfa = "matriz_cuadrada_"+str(o)+"x"+str(o)+".txt"
    f = open(nfa,"r")
    print(f.read())
    f.close()

# Variables globales
M = [] # Matriz
tam_mat = 0 # número de filas o columnas

# Menú de opciones
op = ""
while op!="5":
    print("\nMATRIZ CUADRADA\
           \n1. Generar la matriz\
           \n2. Mostrar la matriz\
           \n3. Guardar la matriz en archivo\
           \n4. Recuperar la matriz del archivo\
           \n5. Salir")
    op = input("Opción? ")
    if op=="1":
        tam_mat = int(input("Ingrese el tamaño de la matriz (máximo 100): "))
        genera_matriz(M,tam_mat)
    elif op=="2":
        mostrar_matriz(M,tam_mat)
    elif op=="3":
        guardar_mat_archivo(M,tam_mat)
    elif op=="4":
        recuperar_mat_archivo(tam_mat)
    elif op=="5":
        print("Programa terminado...\n\n\n")
        time.sleep(1)
        os.system("cls")
