#Ordenar tres números
primer = eval(input("Ingrese el primer numero: "))
segundo = eval(input("ingresa el segundo numero: "))
tercer = eval(input("Ingresa el tercer numero: "))

if primer <= segundo <= tercer:
    print(primer,",",segundo,",",tercer)
    
elif primer <= tercer <= segundo:
    print(primer,",",tercer,",",segundo)

elif segundo <= primer <= tercer:
    print(segundo,",",primer,",",tercer)

elif segundo <= tercer <= primer:
    print(segundo,",",tercer,",",primer)

elif tercer <= primer <= segundo:
    print(tercer,",",primer,",",segundo)

elif tercer <= segundo <= primer:
    print(tercer,",",segundo,",",primer)
