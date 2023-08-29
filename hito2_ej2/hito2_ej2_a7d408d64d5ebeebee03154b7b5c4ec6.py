lista=['a','c','t','g','A','C','T','G']
secuencia=input("Ingresar secuencia: ")
letras=list(secuencia)
if letras in lista:
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")