#Contestador de celular
def cifras():
    global numero 
    numero=int(input("Ingrese el numero adecuado min(8 digitos)"))
    while numero<=10000000:
        numero=int(input("El numero que usted ingreso no cumple con los 8 digitos solicitados"))
        if numero > 9999999:
        
            break
    return numero
def hora():
    global hora
    hora= int(input("Ingrese a hora de la llamada"))
    return hora
def variables_de_horas():
    #False es no contesar 
    #True es contesar 
    global x
    if 19 <= hora:
        x = False
    elif 0 <= hora and hora <= 7:
        x= True
    elif hora<14:
        x = False
    elif hora > 14 and hora < 17:
        x= False
    elif hora >= 17 and hora <= 19 :
        x=True
    #a
    return x 
def contestar(x, numero):
    if x == False :
        unidad=int(str(numero)[-1])
        decima=int(str(numero)[-2])
        centesima=int(str(numero)[-3])
        uni2=int(str(numero)[0])
        deci2=int(str(numero)[1])
        centi2=int(str(numero)[2])
        if unidad == 9 and decima == 0 and centesima == 9 :
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    elif x == True:
        uni2=int(str(numero)[0])
        deci2=int(str(numero)[1])
        centi2=int(str(numero)[2])
        if uni2== 8 and deci2== 7 and centi2== 7:
            
            print("NO CONTESTAR")
        else:
            print("CONTESTAR")
cifras()
hora()
variables_de_horas()
contestar(x,numero)     