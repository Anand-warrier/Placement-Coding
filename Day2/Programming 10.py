n=int(input())
s=0.0
c=n
while(n>0):
    num=float(input())
    s+=num
    n-=1
print(f"The average is: {s/c:.3f}")
    
