secuencia=str(input("Por favor ingrese una secuencia:"))

lista1=["b","d","e","f","h","i","j","k","l","m","n","o","p","q","r","s","u","v","w","x","y","z"]
lista2=["B","D","E","F","H","I","J","K","L","M","N","O","P","Q","R","S","U","V","W","X","Y","Z"]

def genoma(secuencia):
    Adenina= "A" in secuencia
    adenina= "a" in secuencia
    Timina= "T" in secuencia
    timina= "t" in secuencia
    Citosina= "C" in secuencia
    citosina= "c" in secuencia
    Guanina= "G" in secuencia
    guanina= "g" in secuencia

    for i in lista1 or i in lista2:
        if i in secuencia:
            return("Secuencia Incorrecta")
        if (i in secuencia)==False :
            if((Adenina==True or adenina==True)and(Timina==True or timina==True) and (Citosina==True or citosina==True) and (Guanina==True or guanina==True)):
                return("Secuencia correcta")
            if(Adenina==True or adenina==True):
                return("Secuencia correcta")
            if(Timina==True or timina==True) :
                return("Secuencia correcta")
            if(Citosina==True or citosina==True):
                return("Secuencia correcta")
            if(Guanina==True or guanina==True):
                return("Secuencia correcta")
            

    

print(genoma(secuencia))      