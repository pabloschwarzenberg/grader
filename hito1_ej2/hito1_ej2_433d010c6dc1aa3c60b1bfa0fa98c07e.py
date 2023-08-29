#Contestador de celular
numerotelefonico=input("¿Cuál es el número telefonico?\n+569")
x=numerotelefonico
hora=int(input("Hora realizada la llamada: \n"))
lenNum=len(x)
InicioNum=x[0:3]
FinalNum=x[5:9]
inicio=877
while ((lenNum<9) and hora<24):
    if(hora<=7):
        print("Contestar porque podría ser una emergencia")
        break
    elif(hora<14 or FinalNum==909):
        print("Contestar")
        break
    elif(hora<14 and FinalNum!=909):
        print("No contestar")
        break
    elif(17<=hora<=19 and ((int(numerotelefonico[0])==8) and (int(numerotelefonico[1])==7) and (int(numerotelefonico[2])==7))):
        print("No contestar")
        break
    elif(17<=hora<=19 and ((int(numerotelefonico[0])!=8) and (int(numerotelefonico[1])!=7) and (int(numerotelefonico[2])!=7))):
        print("Contestar")
        break
    elif(hora>=19):
        print("No contestar")
        break
else:
    print("Número o hora ingresada no son validas. \n")