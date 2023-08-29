#Contestador de celular
t = int(input('Ingrese numero telefonico: '))
h = int(input('Ingrese hora de la llamada: '))
if 10000000 <= t <= 99999999 and 0 <= h <= 23:
    if 0 <= h <= 7:
        print('Resultado: CONTESTAR')
    if 7 < h < 14:
        
        x = t%1000
        
      
        if x == 909:
            print("Resultado: CONTESTAR")
        else: 
            print("Resultado: NO CONTESTAR")
  
    if 14 <= h < 17:
        print("Resultado: NO CONTESTAR")

    if 17 <= h <= 19:

        y = t//100000  
        
        if y == 877:
            print("Resultado: NO CONTESTAR")
        else:
            print("Resultado: CONTESTAR")
        
    
    if 19 < h :
        print("Resultado: NO CONTESTAR")       