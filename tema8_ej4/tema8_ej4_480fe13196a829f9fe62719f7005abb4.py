def rot13(palabra):
    palabra1=palabra.replace('a', '%temp%').replace('n', 'a').replace('%temp%', 'n')
    palabra2=palabra1.replace('b', '1').replace('o', 'b').replace('1', 'o')
    palabra3=palabra2.replace('c', '2').replace('p', 'c').replace('2', 'p')
    palabra4=palabra3.replace('d', '3').replace('q', 'd').replace('3', 'q')
    palabra5=palabra4.replace('e', '%').replace('r', 'e').replace('%', 'r')
    palabra6=palabra5.replace('f', '%temp').replace('s', 'f').replace('%temp', 's')
    palabra7=palabra6.replace('g', '%tem').replace('t', 'g').replace('%tem', 't')
    palabra8=palabra7.replace('h', '%te').replace('u', 'h').replace('%te', 'u')
    palabra9=palabra8.replace('i', '%t').replace('v', 'i').replace('%t', 'v')
    palabra10=palabra9.replace('j', '%temp%1').replace('w', 'j').replace('%temp%1', 'w')
    palabra11=palabra10.replace('k', '%temp%2').replace('x', 'k').replace('%temp%2', 'x')
    palabra12=palabra11.replace('l', '%temp%3').replace('y', 'l').replace('%temp%3', 'y')
    palabra13=palabra12.replace('m', '%temp%4').replace('z', 'm').replace('%temp%4', 'z')
    return(palabra13)