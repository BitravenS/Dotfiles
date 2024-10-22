import string

def main():
    s = input("Donnez une chaine: ").upper()
    print(s==s[::-1])



if __name__=='__main__':
    main()