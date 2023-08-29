def jerigonzo(a):
    vocal = ['a','e','i','o','u']
    ret = a
    for z in range(len(a)):
        z += (len(ret) - len(a))
        for i in range(5):
            if vocal[i] == ret[z]:
                ret = ret[:z] + vocal[i] + 'p' + ret[z:]
            else:
                pass
    return ret

if __name__ == "__main__":
    pass
         