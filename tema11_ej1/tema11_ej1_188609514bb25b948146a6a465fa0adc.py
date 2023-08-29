def palindromo(palabra):
    a = 0
    for i in range(0,len(palabra)//2):
        if palabra[i] == palabra[-i]:
            a +=1
        else:
            break
    if a < len(palabra)//2:
        return False
    else:
        return True

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           