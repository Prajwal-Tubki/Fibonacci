terms=int(input("Enter the number of terms you want to see in the fibonacci sequnce:"))
j=1
a=0
b=1
c=1
while(j<=terms):
    if j==1:
        print(a)
    elif j==2:
        print(b)
    else:
        print(c)
        a=b
        b=c
        c=c+a
        
        
    j+=1
    
        
        
    
    
    

            
        
    
    
          
