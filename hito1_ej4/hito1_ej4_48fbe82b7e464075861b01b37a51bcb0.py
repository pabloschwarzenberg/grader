x = eval(input("inserte un número: "))


def convertirbinario(d):
    b = ''

    
    while d // 2 != 0:
        b = str(d % 2) + b
        d = d // 2


    return str(d) + b


sf=str(convertirbinario(x))

print("resultado="+sf)