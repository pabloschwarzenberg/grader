valor_a = str(input("secuencia"))
valor_a = valor_a.upper()
valor_b = len(valor_a)
valor_c = 0

for valores in valor_a:
    if valores == "A" or valores == "C" or valores == "T" or valores == "G":
        valor_c = valor_c + 1
        
if valor_c == valor_b:
    print("Secuencia correcta")
    
else:
    print("Secuencia incorrecta")
