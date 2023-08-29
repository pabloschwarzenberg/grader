#Contestador de celular
def contestar_la_llamada(numero_telefono, hora_de_llamado):  
#definir las variables
    if hora_de_llamado >= 0 and hora_de_llamado <= 7:
        print("Contestar")
    elif hora_de_llamado < 14:
        if numero_telefono % 1000 == 909:
            print("Contestar")
        else:
            print("No contestar")
    elif hora_de_llamado >= 17 and hora_de_llamado <= 19:
        if numero_telefono // 87700000 == 1:
            print("No contestar")
        else:
            print("Contestar")
    else:
        print("No contestar")
#colocar los condicionantes con if, elif y else con modulos y division entera para los valores pedidos

numero_telefono = int(input("Ingrese numero del celular: "))
hora_de_llamado = int(input("Ingrese hora de llamada: "))
#preguntar los datos que seran usados 
resultado = contestar_la_llamada(numero_telefono, hora_de_llamado)