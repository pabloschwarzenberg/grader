#Contestador de celular
celu = eval(input("ingrese el numero telefónico: "))
hora = int(input("ingrese la hora de la llamada: "))

if 7 >= hora >= 0:
    print("Resultado: CONTESTAR")
    
if 14 > hora > 7:
    if celu%1000== 909:
        print("Resultado: CONTESTAR")
    else: print("Resultado: NO CONTESTAR")
        
if 17 <= hora <= 19:
    if 878>celu/100000>876:
        print("Resultado: NO CONTESTAR")
    else:
        print("Resultado: CONTESTAR")
        
if 19 < hora:
    print("Resultado: NO CONTESTAR")