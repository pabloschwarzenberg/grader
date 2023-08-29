#Contestador de celular
def Contestar(n,h):
    if(h >=0 and h <=7):
        print("CONTESTAR")
    elif(h >7 and h <=14):
        if(n[5:8]=="909"):
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    elif(17<=h and 19>=h):
        if(n[0:3]=="877"):
            print("NO CONTESTAR")
        else:
            print("CONTESTAR")
    elif(19<h and 23>=h):
        print("NO CONTESTAR")
    return

numero = input("Ingrese numero Telefonico: ")
Hora = int(input("Ingrese hora de la llamada :"))
Contestar(numero,Hora)