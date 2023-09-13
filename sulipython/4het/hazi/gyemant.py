import sys

def main():

    n = input("mag: ")

    for i in range(n):
        print('*')
        if i < n-((n-1)/2):
            print('+')
        else:
            print('-')

    h = eval(input("magassag: "))

    for i in range(h):
        print(" " * (h - i), "*" * (2*i + 1))
    for i in range(h -2, -1, -1):
        print(" " * (h - i), "*" * (2*i + 1))

if __name__ == '__main__':
    main()