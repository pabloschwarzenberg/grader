def buscarTodas(a,b):
    apariciones=[]
    for i in range (0,len(a)):
        if a[i]==b:
            apariciones.append(i)
    out=" "
    for i in apariciones:
        out+=str(i)+" "
        out=out.strip()
    aparicioness=' '.join(map(str,apariciones))
    return aparicioness
if __name__ == "__main__":
   buscarTodas("tres tristes tigres","t")
   pass
           