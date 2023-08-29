def numero_perfecto(a):
    list1 = [1]
    for i in range(2, a + 1):
        if a % i == 0:
            list1.append(i)
            if a in list1:
                list1.remove(a)
                if sum(list1) == a:
                    return True
                else:
                    return False
if __name__ == "__main__":
    print(numero_perfecto(a))

