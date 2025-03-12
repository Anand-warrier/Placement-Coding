#Programming Q19
str1 = input()
t = 0  
avail = 0  

for i in str1:
    if i == "C" or i == "U":
        if avail > 0:
            avail -= 1  
        else:
            t += 1  
    elif i == "R" or i == "L":  
        avail += 1

print(t)
