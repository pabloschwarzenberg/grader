#Descomponer un número
num=input("Ingrese un número: ")
#num tiene que ser si o si un string en el caso de juntar strings
if(len(num)>=1):
    decomp=num[-1]+"U"
if(len(num)>=2):
    decomp=num[-2]+"D + "+decomp
if(len(num)>=3):
    decomp=num[-3]+"C + "+decomp
if(len(num)>=4):
    decomp=num[-4]+"M + "+decomp
# los espacios en los strings de arriba son importantes para que el programa pueda verificar bien los strings
# anteriormente este me los anulaba al igual que los del zodiaco con mayúsculas
print(decomp)
