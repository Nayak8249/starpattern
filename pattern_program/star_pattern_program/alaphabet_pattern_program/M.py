for i in range(7):
    for j in range(7):
        if (j==0 )or (j==6) or ( i+j==6  and 3>=i) or (i==j and 3>=i ):
            print('*',end=" ")
        else:
            print(' ',end=" ")    
    print()        