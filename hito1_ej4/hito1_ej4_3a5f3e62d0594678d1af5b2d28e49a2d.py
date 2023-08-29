def b(decimal):
    bi=""
    while decimal //2!=0:
        bi=str(decimal%2)+bi
        decimal=decimal//2
    return str(decimal)+bi
numero=int(input())
print("resultado=",b(numero))