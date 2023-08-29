secuencia = input("Ingrese su secuencia de letras:")
letras_distintas = 0
for letra in secuencia:
    if((letra!="A")and(letra!="C")and(letra!="T")and(letra!="G")and(letra!="a")and(letra!="g")and(letra!="t")and(letra!="c")):
         letras_distintas = letras_distintas + 1
         print(letras_distintas)
    else:
         letras_distintas = 0
if letras_distintas == 0:
        print("Secuencia correcta")
else:
        print("Secuencia incorrecta")
        
        
          