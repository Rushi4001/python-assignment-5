
digit=0
sum=0

def reverse(ino):
    global digit,sum
    if(ino>0):
       
        digit=(ino%10)
        ino=ino/10
        sum=sum+digit
        reverse(int(ino))
    return sum    
        
        
        
def main():
    
    value=int(input())
    
    bret=reverse(value)
    print("sum of digit",bret)


if __name__=="__main__":
    main()