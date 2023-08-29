def suma_divisores(a):
    d=1
    s=0
    while d<a:
      if a%d==0:
        s=s+d
      d=d+1
    #faltaba que retornara el segundo valor
    return s,primo(a)

def primo(a):
    d=1
    s=0
    while d<a:
      if a%d==0:
        s=s+d
      d=d+1
    if s==1:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    #la función debe retornar como resultado dos valores, aquí se está imprimiendo el valor
    #print("(",suma_divisores(a),",",primo(a),")")
    print(suma_divisores(a))


           