def lin(res , key):
    p=0
    for i in range(0,len(res)):
       if(res[i] == key):
            p=1
            print("found")
    if(p==0):
        print("not found")
        
res= []
nums = int(input("enter the no of elements"))
print("enter the values")
for i in range(0 , nums):
     ll=int(input())
     res.append(ll)
key = int(input("enter the key value"))
lin(res, key)
