#Contestador de celular
seguir = True
while(seguir):
    n = input("ingrese numero de telefono: ")
    if(len(n)>8 or len(n)<8):
        print("ingrese correctamente los digitos")
    else:
        seguir = False
        h = int(input("ingrese la hora de llamada "))
        if(h>24 or h<00):
            print("ingrese hora valida")
        elif(h>=00 and h<=7):
            print("contestar")
        elif(h<14):
            if(n[5]=="9" and n[6]=="0" and n[7]=="9"):
                print("contestar")
            else:
                print("no contestar")
        elif(h>=17 and h<=19):
            if(n[0]=="8" and n[1]=="7" and n[2]=="7"):
                print("no contestar")
            else:
                print("contestar")
        elif(h>19 or h<00):
            print("no contestar")