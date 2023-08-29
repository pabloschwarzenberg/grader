def rot13(palabra):
    normal = "abcdefghijklmnopqrstuvwxyz"
    elcodigosecreto=""
    for i in palabra:
        transformacion = normal.find(i)+13
        m = int(transformacion)%len(normal)
        elcodigosecreto = elcodigosecreto + str(normal[m])
    return elcodigosecreto
    