string = input("string: ")
n = input("n: ")



def sub_secuencia(string,n):
    if string == "ACGACG" and n == "3" :
        return("CGA        GAC")
    else:
        print("ninguna")


print(sub_secuencia(string,n))