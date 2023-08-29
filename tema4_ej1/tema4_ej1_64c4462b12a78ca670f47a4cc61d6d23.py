from random import randint
secret = ['loco', 'perro', 'gato', 'paralelepipedo', 'costumbre', 'supernumeral']

def ocultar_letras(palabra,cantidad):
    for i in range(cantidad):
         a = randint(1,len(palabra) - 1)
         if a < len(palabra) - 1:
             palabra = palabra[:a] + '_' + palabra[(a + 1):]
         else:
             palabra = palabra[:a] + '_'
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    if len(letra) == 1:
        a = []
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] != palabra[i]:
                a.append(palabra_secreta[i])
            else:
                pass
        if letra in a and len(a) == 1:
            return palabra_secreta
        elif letra in a and len(a) != 1:
            n = 0
            for i in range(len(a)):
                if letra == a[i]:
                    b = n
                    n = palabra[b:].find(a[i])
                    palabra_secreta += palabra_secreta[b:n] + a[i] + palabra_secreta[n+1:]
                else:
                    pass
        else:
            return palabra
    else:
        if letra == palabra:
            return palabra
            
if __name__ == "__main__":
    pass
         