def palindromo(palabra):
    palabra1=[]
    for i in reversed(palabra):
        palabra1.append(i)
    palabra1="".join(palabra1)
    if palabra1==palabra:
        return True
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           

           