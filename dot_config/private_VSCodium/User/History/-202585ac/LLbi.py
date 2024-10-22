import string

def main():
    s = input("Donnez une chaine: ")
    return s==s[::-1]



if __name__=='__main__':
    main()