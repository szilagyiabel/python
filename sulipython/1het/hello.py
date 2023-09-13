import sys

def hello(name):
    if name == 'Batman' or name == 'Robin':
        print ('denevérveszély')

def main():
    hello(sys.argv[1])

if __name__ == "__main__":
    main()