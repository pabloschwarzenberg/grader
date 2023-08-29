def suma_divisores(S):
    suma_de_numeros=0
    numero_primo=False
    for i in range(1,S):
        if S%i==0:
            suma_de_numeros=i+suma_de_numeros
    if suma_de_numeros==1:
        numero_primo=True
    return suma_de_numeros, numero_primo

print(suma_divisores(6))