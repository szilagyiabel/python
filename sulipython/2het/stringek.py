def hello(name, color, what):
    print("{0}, {1} az {2}".format(name, color, what))
    print("{nev}, {szin} az {mi}".format(nev=name, szin=color, mi=what))

def main():
    hello("kabel", "zöld", "egg")

if __name__ == '__main__':

    main()