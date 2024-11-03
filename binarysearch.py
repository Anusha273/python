def bin(ele, key,low , high):
   mid= (low + high) // 2
   
   if(ele[mid]==key):
           print(mid)
   elif(ele[mid]<key):
         bin(ele,key,low,mid-1)
   elif(ele[mid]>key):
         bin(ele,key,mid+1,high)
                      

res= []
nums = int(input("enter  numbers"))
for i in range(0 , nums):
     ll=int(input())
     res.append(ll)
key = int(input("enter a key value"))
ele = []
ele = sorted(res)
low = 0
bin(ele , key , low , nums-1) 
