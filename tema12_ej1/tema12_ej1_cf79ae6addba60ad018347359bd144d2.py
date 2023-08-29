def combinacion(n,nuevo=""):
    if len(nuevo)==n:
        print(nuevo)
        return
    numeros=["0","1"]
    for i in numeros:
        nuevo=nuevo+i
        combinacion(n,nuevo)
        nuevo=nuevo[:len(nuevo)-1]
n=int(input())
combinacion(n)
           