prices=list(map(int,input().split(",")))
buy=float('inf')
maxp=0
for i in prices:
    if i<buy:
        buy=i
    else:
        if i-buy>maxp:
            maxp=i-buy
print(maxp)
