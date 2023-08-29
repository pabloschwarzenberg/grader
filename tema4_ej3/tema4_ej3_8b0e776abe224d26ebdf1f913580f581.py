# Declaración de la función
def jerigonzo(texto):
    n_texto = "" # acumulador o concatenador
    for c in texto:
        if c=="a" or c=="A":
            n_texto = n_texto + c + "p" + c
        elif c=="e" or c=="E":
            n_texto = n_texto + c + "p" + c
        elif c=="i" or c=="I":
            n_texto = n_texto + c + "p" + c
        elif c=="o" or c=="O":
            n_texto = n_texto + c + "p" + c
        elif c=="u" or c=="U":
            n_texto = n_texto + c + "p" + c
        else:
            n_texto = n_texto + c
    return n_texto
# Programa principal
print("Jerigonzo")
op = "S"
while op=="S":
    # Captura de datos
    s = input("Ingrese su mensaje:")
    # Procesamiento
    mj = jerigonzo(s) # Invocación de la función
    # Exposición del resultado
    print("Su mensaje en Jerigonzo: ",mj)
    op = input("Ejecutar otra vez? S/N:")
    op = op.upper()