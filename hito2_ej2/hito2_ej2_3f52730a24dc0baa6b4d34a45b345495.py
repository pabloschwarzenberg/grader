def validar_secuencia(s):
    contador=0
    for i in s:
        if i=="A" or i=="C" or i=="T" or i=="G":
            contador=contador+1
        else:
            return print("la secuencia",s,"es incorrecta")
    if contador==len(s):
        return print("la secuencia",s,"es correcta")

if __name__ == "__main__":
    Z=input("metele secuencia: ")
    Z=Z.upper()
    validar_secuencia(Z)