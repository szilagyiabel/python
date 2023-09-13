
def main():
    mely = 0
    magas = 0
    vegyes = 0

    f = open("words.txt", "r")
    for line in f:
        line = line.rstrip("\n")
        
        mely0 = False
        magas0 = False

        if 'a' in line or 'o' in line or 'u' in line:
            mely0 = True
        if 'e' in line or 'i' in line:
            magas0 = True
        if mely0:
            if magas0:
                vegyes += 1
            else:
                mely += 1
        if magas0 and not mely0:
            magas += 1
        
    print("magas szavak: ", magas)
    print("mely szavak: ", mely)
    print("vegyes szavak: ", vegyes)           

    f.close()

if __name__ == '__main__':
    main()