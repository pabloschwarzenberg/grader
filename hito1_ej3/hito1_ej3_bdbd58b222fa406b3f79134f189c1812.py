#Aprobación de créditos
ingreso = eval(input("ingresa tu ingreso: "))
nacimiento = eval(input("ingresa tu año de nacimiento: "))
hijos = eval(input("ingresa tu cantidad de hijos: "))
banco = eval(input("ingresa tus años en ek banco: "))
estado = str(input("ingresa tu estado civil (C) o (S): "))
vive = str(input("vives en zona urbana(U) o zona rural(R): "))
edad = 2022-nacimiento

if banco > 10 and hijos >= 2:
    print( "APROBADO")

elif estado == "C" and hijos > 3 and edad >= 45 and edad <=55:
        print( "APROBADO")
        
elif ingreso > 2500000 and estado == "S" and vive == "U":
        print ("APROBADO")
        
elif ingreso > 3500000 and banco > 5:
    print ("APROBADO")
    
elif vive == "R" and estado == "C" and hijos < 2:
    print ("APROBADO")

else:
    print ("RECHAZADO")
      