def decodificar(s):
    s1=""
    s=s.split(",")
    for i in s:
        j=int(str(i),2)
        s1+=chr(j)
        
    return s1



if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         