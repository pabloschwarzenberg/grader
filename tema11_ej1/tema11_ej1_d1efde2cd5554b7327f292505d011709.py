A = None
def palindromo(palabra):
    global A 
    palabra = list(palabra)
    
    if len(palabra) == 1:
        A = True
    elif palabra[0] == palabra[-1]:
        palabra.remove(palabra[0])
        
        palabra = palabra.pop()
        
        palabra = "".join(palabra)
        
        palindromo(palabra)
    else:
        A = False
    return A
if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           