secuencia = input()
def validar_secuencia(s):
    r= s.upper()
    valida = False
    if len(r) == 4:
        if r.find("A") != -1:
            if r.find("C") != -1:
                if r.find("T") != -1:
                    if r.find("G") != -1:
                        valida= True
    return(valida)

if validar_secuencia(secuencia):
    print("secuencia correcta")
else:
    print("secuencia incorrecta")