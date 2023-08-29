secuencia=input("Ingrese secuencia: ")
sec=""
valida="actgACTG"
for letra in secuencia:
    if letra in valida:
        sec+=letra
    else:
            print("incorrecta")
    
print("correcta")      