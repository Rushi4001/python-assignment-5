
def pattern(i):
    if (0<i):
        print("*",end="")
        i=i-1
        pattern(i)

        
    
def main():
    value=int(input())
    pattern(value)
    
if __name__=="__main__":
    main()

