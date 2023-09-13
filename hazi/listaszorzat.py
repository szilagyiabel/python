def main():
    szam = [1, 2, 3, 4, 5]
    paros = []
    for n in szam:
        if n % 2 == 0:
            paros.append(n)
    print(szam.find("2"))

if __name__ == '__main__':
    main()