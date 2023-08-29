#Contestador de celular
numero=float(input("Ingrese su número de celular:"))
hora=float(input("Ingrese la hora en que recibió la llamada:"))

numero_str=str(numero)
if 0 <= hora <= 7:
    print("CONTESTAR")
elif 8 <= hora <= 14:
    if numero_str[5:8]=="909":
        print("CONTESTAR")
    else :
        print("NO CONTESTAR")
elif 14<=hora<17:
    print("NO CONTESTAR")
    
elif 17 <= hora <= 19:
    if numero_str[0:3]=="877":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
 
elif 19 <= hora <= 23:
    print("NO CONTESTAR")

