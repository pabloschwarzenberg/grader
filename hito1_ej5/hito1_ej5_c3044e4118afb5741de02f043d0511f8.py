#Cálculo del dígito verificador de un rut
x = int(input("Infrese el RUT --> ")) # 211588799

texto = str(x)

if len(str(x)) == 8:
    uno = texto[7]
    dos = texto[6]
    tres = texto[5]
    cuatro = texto[4]
    cinco = texto[3]
    seis = texto[2]
    siete = texto[1]
    ocho = texto[0]
   
    suma = int(uno)*2 + int(dos)*3 + int(tres)*4 + int(cuatro)*5 + int(cinco)*6 + int(seis)*7 + int(siete)*2 + int(ocho)*3 
    q = suma%11
    digito = 11 - q
        
    if digito == 10:
        print("dv=K")
        
    if digito == 11:
        print("dv=0")
    
    if digito < 10:
        print("dv="+str(digito))
        
if len(str(x)) == 7:
    uno = texto[6]
    dos = texto[5]
    tres = texto[4]
    cuatro = texto[3]
    cinco = texto[2]
    seis = texto[1]
    siete = texto[0]
   
    suma = int(uno)*2 + int(dos)*3 + int(tres)*4 + int(cuatro)*5 + int(cinco)*6 + int(seis)*7 + int(siete)*2  
    q = suma%11
    digito = 11 - q
       
    if digito == 10:
        print("dv=K")
        
    if digito == 11:
        print("dv=0")
    
    if digito < 10:
        print("dv="+str(digito))
        