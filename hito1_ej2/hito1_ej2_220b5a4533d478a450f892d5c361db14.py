#Contestador de celular
n = int(input("Ingrese su numero telefonico 8 digitos :"))
h = int(input("Ingrese hora de llamada 0 al 23 hrs :"))

if(0<=h<=7):
    print("CONTESTAR")
elif(7<h<14) and (n%1000==909):
    print("CONTESTAR")
elif(17<=h<=19) and (n//100000==877):
    print("NO CONTESTAR")
elif(17<=h<=19):
    print("CONTESTAR")
elif(19<h):
    print("NO CONTESTAR")
elif(h<23):
    print("sus horas no son validas")
elif(h<0):
    print("sus horas no son validas")
elif(n<99999999):
    print("su numero telefonico no es valido")

