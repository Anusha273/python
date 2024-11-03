n = int(input("how many num u want to enter"))
nums=[]
print("enter the values")
for i in range(0, n):
    ns = int(input())
    nums.append(ns)
print("before sorting the list of elemnets are:")
print(nums)
for i in range(len(nums)):
  for j in range(0 , len(nums)-1):
     if(nums[j] > nums[j+1]):
        temp = nums[j]
        nums[j]=nums[j+1]
        nums[j+1]= temp
print("after the sorting the list of elements are:")
print(nums)




    
    
