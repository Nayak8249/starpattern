for num in range(1,100):
    fcount=0
    for i in range(1,num+1):
        if num%i==0:
            fcount+=1
    if fcount==2:
        print(num,end=' ')             