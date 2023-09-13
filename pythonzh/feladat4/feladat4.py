def main():
    x = 1
    sztringek = []
    j = 1

    for i in range(200):
        print("Kérem adja meg az", x,". szót: ", end = '')
        sztring = input()
        sztringek.append(sztring)

        x += 1
        
        if '*' in sztring:
            print("VÉGE")
            print("A leghosszabb sztringek: ")
            for j in range(3):
                if len(sztringek[j]) > len(sztringek[j + 1]):
                    print(j + 1)
                    print(sztringek)
            exit(1)

    
if __name__ == '__main__':
    main()