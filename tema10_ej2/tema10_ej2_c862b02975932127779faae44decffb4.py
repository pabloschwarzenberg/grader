def levenshtein(palabra1, palabra2):
        if palabra1 == palabra2:
            return "0D"
        palabra1l = list(palabra1)
        palabra2l = list(palabra2)
        cont_letras = 0
        if len(palabra1)>len(palabra2):
          for i in range(len(palabra2l)):
            if palabra2l[i] != palabra1l[i]:
                cont_letras += 1
        else:
            for i in range(len(palabra1l)):
                if palabra1l[i] != palabra2l[i]:
                    cont_letras += 1

        if len(palabra1) - len(palabra2) > 1 or (cont_letras > 1 and (len(palabra1)-len(palabra2)<-1)or len(palabra1) - len(palabra2) > 1 ) or len(palabra1)-len(palabra2)<-1:
            return "+1"
        else:
            if (len(palabra1) - len(palabra2) == 1 or len(palabra1) - len(palabra2) ==-1) and cont_letras<3:
                return "IB"
            elif cont_letras == 1:
                return "1S"
            elif cont_letras==1 and len(palabra1)==len(palabra2):
                return "1S"
            else:
                return "+1"


            


if __name__ == "__main__":
    lev1=input('Palabra 1?')
    lev2=input("Palabra 2?")
    print(levenshtein(lev1,lev2))
    