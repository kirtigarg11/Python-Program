
ar=input().split(" ")
ar1=[]
ar2=[]
inde=0
for i in ar:
    ar1.append(len(i))
    ar2.append(i)
ma=0   
for i in range(len(ar1)):
    if(ar1[i]>ma):
        ma=ar1[i]
        inde=i
print(ar2[inde])
    
