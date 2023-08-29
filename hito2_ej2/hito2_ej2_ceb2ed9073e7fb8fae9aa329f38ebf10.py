def genoma(palabra):
    if len(palabra) == 4 and "a" in palabra and "c" in palabra and "t" in palabra and "g" in palabra :
        print("Secuencia correcta")
    elif "a" is not palabra and "c" is not palabra and "t" is not palabra and "g" is not palabra:
        print("Secuencia incorrecta")
  
print(genoma(input("Ingrese palabra :")))  