def numero_perfecto(numero):
    num_a = []
    num_b = []
    result = []
    for i in range(1, numero):
        if numero % i == 0:
            num_a.append(i)
            num_b.append(i)
    for i in num_a:
        if i in num_b:
            result.append(i)
    if sum(result) == numero:
        return True
    return False

if __name__ == "__main__":
    print(numero_perfecto(6))