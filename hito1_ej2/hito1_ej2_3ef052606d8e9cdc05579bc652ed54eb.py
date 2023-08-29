#Contestador de celular
numero= input("ingrese un numero de 8 digitos" )
hora=int(input("ingrese hora de llamada (horario 24 horas)" ))

if hora <= 7:
    print("CONTESTAR")
elif hora <= 14:
    if numero.endswith("909"):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if 17 <= hora >= 19:
    print("NO CONTESTAR")
elif numero.startswith("877"):
    print("NO CONTESTAR")
if hora > 19: 
    print("NO CONTESTAR")           