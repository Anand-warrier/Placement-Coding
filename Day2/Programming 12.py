n=int(input())
for i in range(2,n//2+1):
    if n%i==0:
        print(n,"is not a prime number" )
        exit(0)
print(n,"is a prime number")        
