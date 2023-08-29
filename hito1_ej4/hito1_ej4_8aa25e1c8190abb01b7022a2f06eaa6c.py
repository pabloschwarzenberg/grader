def dab(N):
    if N <= 0:
        return "0"
    B = ""
    while N > 0:
        R = int(N % 2)
        N = int(N / 2)
        B = str(R) + B
    return B

N = int(input("Ingrese un digito: "))        
B = dab(N)
print("Resultado=",B) 