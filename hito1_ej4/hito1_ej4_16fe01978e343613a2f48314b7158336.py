def binarizar(decimal):
        binario = ""
        while decimal//2 != 0:
              binario = str(decimal%2)+binario
              decimal = decimal//2
        return str(decimal) + binario
decimal = int(input("Ingrese el numero que desea convertir a binario:"))
print("resultado=",binarizar(decimal))

         
         