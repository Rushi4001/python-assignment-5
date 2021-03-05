

def reverse(i):
    if(i>0):
        print(i,end="")
        i=i-1
        reverse(i)

def main():
    value=int(input())
    
    reverse(value)



if __name__=="__main__":
    main()