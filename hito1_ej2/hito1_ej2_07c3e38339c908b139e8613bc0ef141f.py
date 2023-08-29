#Contestador de celular
Numero= input("Ingrese Numero: ")
Hora= int(input("Ingrese Hora: "))

NumeroCortadoI= int(Numero[0: 3: 1])
NumeroCortadoF= int(Numero[5: 8: 1])

if (0<Hora and Hora<=7):
    print("Resultado: Contestar ")

if (7<Hora and Hora<14 and NumeroCortadoF==909):
    print("Resultado: Contestar ")
    
if (7<Hora and Hora<14 and NumeroCortadoF!=909):
        print("Resultado: No Contestar ")
        
if (14<=Hora and Hora<17):
    print("Resultado: No Contestar ")

if (17<=Hora and Hora<=19 and NumeroCortadoI==877):
    print("Resultado:No Contestar ")
    
if (17<=Hora and Hora<=19 and NumeroCortadoI!=877):
    print("Resultado: Contestar ")

if (19<Hora):
    print("Resultado: No Contestar ")