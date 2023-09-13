def draw_tabla(s):
    
    for i in range(10):
        if i == 0:
            print("+" + "-"*17 +"+")
            continue
        elif i == 9:
            print("+" + "-"*17 +"+")
            break
        print("|" + " ."*8 +" |")

    szamok = []

    for i in sorted(s)[::-1]:
        szamok.append(s.index(i))

    print(szamok)

    print("+" + "-"*17 +"+")

    for i in range(8):
        print("|", end=" ")
        for j in range(8):
            if j == szamok[i]:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print("|")

    print("+" + "-"*17 +"+")

def main():

    kir = [7,3,0,2,5,1,6,4]

    tabla = list(range(1, 19, 1))
    draw_tabla(kir)


if __name__ == '__main__':
    main()