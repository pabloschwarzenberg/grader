import random

def ocultar_letras(palabra,cantidad):
    P = list(palabra)
    i = 0
    nums = []
    while i < cantidad:
        c = random.randint(0,len(P)-1)
        if c not in nums:
            P[c] = "_"
            nums.append(c)
        else:
          c = random.randint(0,len(P)-1)
          continue
        i += 1
    
    return "".join(P)

def revisar_letra(palabra_secreta,palabra,letra):
    P = list(palabra_secreta)
    L = list(palabra)
    for i in range(len(P)):
        if P[i] == letra and letra != L[i]:
            L[i] = letra
    return "".join(L)

if __name__ == "__main__":
    pass
         