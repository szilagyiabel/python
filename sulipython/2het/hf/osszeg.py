
import sys


def main():
    if len(sys.argv) != 3:
        print("kettőt adj meg")
        exit(1)
    
    x = int(sys.argv[1])
    y = int(sys.argv[2])

    print(x + y)

if __name__ == '__main__':
    main()