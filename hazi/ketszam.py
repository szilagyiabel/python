import sys

def main():

    if len(sys.argv) != 3:
        print("hiba, kettőt adj meg")
    else:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        print(x + y)

if __name__ == '__main__':
    main()