def rot13(palabra):
    alfabeto="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    i=0
    while i<len(palabra):
        r= alfabeto.find(palabra[i])
       # palabra=palabra.replace(palabra[i],alfabeto[r+13])
        palabra= palabra[:i]+alfabeto[r+13] + palabra[i+1:]
        i=i+1
    return palabra