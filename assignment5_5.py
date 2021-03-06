
digit=1
def fact(ino):
    global digit
    if (ino>0):
        digit=digit*ino
        ino=ino-1
        fact(ino)
    return digit   
    
def main():
    value=int(input())
    
    ret=fact(value)
    print("factorial is:",ret)


if __name__=="__main__":
    main()
    