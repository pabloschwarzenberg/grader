def dec_to_bin(x):
    return int(bin(x)[2:])

a=int(input("ingrese un numero: "))
b=dec_to_bin(a)
print ('resultado=%d'%(b)) 
