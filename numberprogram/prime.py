
n=int(input())
fcount=0
for i in range(1,n+1):
    if n%i==0:
        fcount+=1
if fcount==2 :
     print(n,'prime number')    
else:
    print (n,"composite number ")    
'''''''''''   
"""def prime(n,fcount=0):
    for i in range(1,n+1):
        if n%i==0:
            fcount+=1
    return fcount 
if prime ==2:
    print('prime number ')  
    
print(prime(7))          

def isprime(num):
    if num <2:
        return ("non_prime")
    for i in range(2,num):
        if num%i ==0:
            return ("non prime")
    return ("prime")
print(isprime(1))
'''''''''


                