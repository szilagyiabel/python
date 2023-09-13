import sys

def megfor(n):
    return int(str(n)[::-1])

def main():

    x = sys.argv[1]
    print(x)
    print(megfor(x))

if __name__ == '__main__':
    main()
