def main():
    f = open("szoveg2.txt", "a")

    print("Elso sor", file = f)
    print("Masodik sor", file = f)
    print("Harmadik sor", file = f)

    f.write("Cica\n")

    f.close()

if __name__ == '__main__':
    main()