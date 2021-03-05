i=1
def display(x):
    if (x>0):
        global i
        print(i,end="")
        i=i+1
        x=x-1
        display(x)
       


def main():
    value=int(input())
    
    display(value)


if __name__=="__main__":
    main()


