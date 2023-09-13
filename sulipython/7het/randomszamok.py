import random

def main():

    print(random.random())
    print(random.randint(1,30))

    szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(szamok)
    random.shuffle(szamok)
    print(szamok)
    print(random.choice(szamok))

if __name__ == '__main__':
    main()