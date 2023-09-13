def draw_dia(hossz, szamok):
    for i in szamok:
        print(("*" * i).center(hossz))

def main():

    n=eval(input("adj meg vmit: "))

    eleje = list(range(1, n + 1,2))
    vege = eleje[:-1][::-1]
    stars=eleje + vege
    draw_dia(n, stars)

if __name__ == "__main__":
    main()
