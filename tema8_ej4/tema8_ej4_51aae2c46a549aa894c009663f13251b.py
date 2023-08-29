# Encriptador ROT13
def rot13(pbra_1):
    alfabeto_am, alfabeto_nz, pbra_2, n = "abcdefghijklm", "nopqrstuvwxyz", "", 0
    
    while n != len(pbra_1):
        for i in range(13):
            if n == len(pbra_1):
                break
            elif pbra_1[n] == alfabeto_am[i]:
                pbra_2, n = pbra_2 + alfabeto_nz[i], n + 1
            elif pbra_1[n] == alfabeto_nz[i]:
                pbra_2, n = pbra_2 + alfabeto_am[i], n + 1
    
    return pbra_2

if __name__== "__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    
    resultado = rot13(palabra)
    
    print("\nEl resultado es:", resultado)