class peldanyok:
    counter = 0

    def __init__(self):
        peldanyok.counter += 1

def main():
    
    p0 = peldanyok()
    p1 = peldanyok()
    p2 = peldanyok()
    p3 = peldanyok()

    print(peldanyok.counter)

if __name__ == '__main__':
    main()