# completa el código de la función
def amigos(a,b):
    incremental=1
    prueba_a=0
    while a//(incremental+1) :
        if a%incremental==0 :
            prueba_a=prueba_a+incremental
        incremental+=1
    incremental=1
    prueba_b=0
    while b//(incremental+1) :
        if b%incremental==0 :
            prueba_b=prueba_b+incremental
        incremental+=1
    if a==prueba_b and b==prueba_a:
        amigos=True
    else:
        amigos=False
    return amigos