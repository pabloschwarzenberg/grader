 palabra = str(input("Ingresa cadena de ADN:"))
if palabra.startswith("A") and palabra.endswith("G"):
    print("Es un genoma")
else:
    print("NO es  un genoma")