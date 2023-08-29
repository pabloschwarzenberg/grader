def palindromo(palabra):
    palabra=list(palabra)
    otra=palabra.copy()
    otra.reverse()
    letra=0
    aux=[]
    if palabra[letra]!=otra[letra]:
        return False
    else:
        while letra<len(palabra):
            if palabra[letra]==otra[letra]:
                aux.append(palabra[letra])
                letra=letra+1
            else:
                return False
    aux=''.join(aux)
    palabra=''.join(palabra)
    if aux==palabra:
        return True
if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           