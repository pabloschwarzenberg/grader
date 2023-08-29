#Contestador de celular
datos = 0
valhora = -1
while datos != 8:
    telefono = int(input("Ingrese número telefonico: "))
    datos = len(str(telefono))
    if datos != 8 :
        print("Por favor ingrese telefono de 8 digitos")  
while valhora < 0 or valhora > 24: 
    hora = int(input("Ingrese la hora de llamada: "))    
    valhora = hora
    if valhora <0 or valhora >24:
        print("Por favor ingrese una hora valida") 
un = telefono%1000
fn = telefono//100000
if valhora > 0 and valhora <7:
    print("CONSTESTAR")
elif valhora > 7 and valhora < 14 and not un == 909:
    print("NO CONTESTAR")
elif valhora > 7 and valhora < 14 and un == 909:
    print("CONTESTAR")        
elif valhora > 17 and valhora < 19 and not fn == 877:
    print("CONTESTAR")
elif valhora > 17 and valhora < 19 and  fn == 877:
    print("NO CONTESTAR")
elif valhora > 19 and valhora < 23:
    print("NO CONTESTAR")