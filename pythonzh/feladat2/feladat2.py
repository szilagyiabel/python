import sys

def karakter_szuro(szo):

    if len(szo) == 2:
        return sys.argv[1]
    else:

        word = szo[1]
        n = [szo[i] for i in range(2,len(szo))]

        for i in n:
            word = word.replace(i,"")
            
        return word

def main():

    eredmeny = karakter_szuro(sys.argv)
    print(eredmeny)

if __name__ == '__main__':
    main()