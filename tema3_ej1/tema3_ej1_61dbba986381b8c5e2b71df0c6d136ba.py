# completa el código de la función
def suma_divisores(a):
    Es_Primo = True
    No_Primo = False
    Lista_1 = [1]
    for A in range(2, a + 1):
        if a % A == 0:
            Lista_1.append(A)
    for B in Lista_1:
        if B == a:
            Lista_1.remove(B)
    if sum(Lista_1) == 1:
        return sum(Lista_1), Es_Primo
    else:
        return sum(Lista_1), No_Primo


