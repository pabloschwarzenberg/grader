# por favor escribe aquí tu función
def es_primo(numero):
    resto = 0
    division = 0
    es_primo = False    
    if(numero > 0):
        for i in range(numero):            
            division = division +1            
            if(division > 1 and division < numero):
                resto = numero % division                
                if(resto > 0):
                    es_primo = True
                else:
                    es_primo = False
                    break
    return es_primo

try:
    entero = int(input("Ingrese Numero :"))
    respuesta = es_primo(entero)
    print(respuesta)
except:
    pass