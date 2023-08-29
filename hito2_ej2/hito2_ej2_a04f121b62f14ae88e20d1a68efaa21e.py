secuencia=input()
if secuencia.count("A")>=0 and secuencia.count("T")>=0 and secuencia.count("G")>=0 and secuencia.count("C")>=1:
    print("secuencia correcta")
else:
    print("secuencia incorrecta")