i=1
def display(x):
    global i
    if (i<=x):
        print(i,end="")
        i=i+1
        #x=x-1
        display(x)
       


def main():
    value=int(input())
    
    display(value)


if __name__=="__main__":
    main()


