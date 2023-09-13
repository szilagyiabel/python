import sys

def karakter_szamlalo(szo):
    dick = {}

    for i in szo:
        if i in list(dick.keys()):
            dick[i] += 1
        else:
            dick[i] = 1

    return dick

def main():
    
    if len(sys.argv) != 2:
        print("hiba, adj meg egy cuccot")
        exit(1)

    sztring = sys.argv[1]

    eredmeny = karakter_szamlalo(sztring)

    for i in eredmeny.keys(): 
        print(i, ' - ',eredmeny[i])

if __name__ == "__main__":
    main()