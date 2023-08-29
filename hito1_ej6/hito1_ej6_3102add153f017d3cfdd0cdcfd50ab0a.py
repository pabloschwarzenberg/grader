#Ordenar tres números
primerNum = int(input("Ingrese primer numero: "))
segundoNum = int(input("Ingrese segundo numero: "))
tercerNum = int(input("Ingrese tercer numero: "))

if primerNum <= segundoNum <= tercerNum:
    print("Los numeros ordenados de menor a mayor es" , primerNum ,",", segundoNum , "," ,tercerNum)

elif segundoNum <= primerNum <= tercerNum:    
    print("los numeros ordenados de menor a mayor es" , segundoNum , "," , primerNum , "," ,tercerNum)
    
elif tercerNum <= primerNum <= segundoNum:
    print("los numeros ordenados de menor a mayor es" , tercerNum , "," , primerNum , "," , segundoNum)

elif segundoNum <= tercerNum <= primerNum:    
    print("los numeros ordenados de menor a mayor es", segundoNum , "," , tercerNum , "," , primerNum)

elif primerNum <= tercerNum <= segundoNum:    
    print("los numeros ordenados de menor a mayor es", primerNum , "," , tercerNum , "," , segundoNum)

elif tercerNum <= segundoNum <= primerNum:    
    print("los numeros ordenados de menor a mayor es" , tercerNum , "," , segundoNum , "," , primerNum)

   