secuencia = input("ingresa la secuencia de ADN: ")

if len(secuencia)%2 == 0:
    letras = "A,C,T,G,a,c,t,g"
    for letra in secuencia:
        if letra in letras:
            print("la secuencia "+secuencia+" es correcta")
        else:
            print("la secuencia "+secuencia+" es incorrecta")
else:
    print("la secuencia "+secuencia+" es incorrecta")
