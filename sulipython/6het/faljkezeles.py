def main():

    f = open("szoveg.txt", "r")
    #for sor in f:
        #print(sor, end="")
        #print(sor.strip("\n"))

    #f.close()

    sorok = [sor.strip("\n") for sor in f.readlines()]
    print(sorok)

    f.close()

if __name__ == '__main__':
    main()