for i in range(7):
    for j in range(7):
        if (j==0 and i+j!=0) or (i==0 and 1<=j<=5)  or (j==6 and i+j!=6) or ( i==4 and 2<=j<=4):
            print( "*",end=" ")
        else:
            print(' ',end=' ')    
    print()        