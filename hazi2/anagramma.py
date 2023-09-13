import sys

def main():

    if len(sys.argv) != 3:
        print("hiba, kettőt adj meg")
        exit(1)

    for i in sys.argv[1:]:
        print(i)
    
    if sys.argv[1] == sys.argv[2]:
        print("anagramma")
    else :
        print("nem anagramma")

if __name__ == '__main__':
    main()