def palindromo(palabra):
        palabra=str(palabra)
        l=[]
        for i in range(len(palabra)):
            l.append(palabra[i])
        l.reverse()
        cand="".join(l)
        if cand==palabra:
            return True
        else:
            return False

    


if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           