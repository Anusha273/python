def swap(nums,a , b):
    temp = nums[a]
    nums[a]=nums[b]
    nums[b]=temp

def partition(nums, l , h):
    pivot = nums[h]
    i = (l-1)
    for j in range(l,h):
        if(nums[j]<pivot):
            i += 1
            swap(nums , i , j)
    swap(nums , i+1, h)
    return (i+1)
    
def quicksort(nums,l ,h):
    if(l<h):
        pi=partition(nums,l,h)
        quicksort(nums,l,pi-1)
        quicksort(nums,pi+1, h)


n= int(input("enter the number of elements:"))
nums=[]
for i in range(n):
    nu = int(input())
    nums.append(nu)
print("before sorting the list of elements are:")
print(nums)
quicksort(nums , 0 , n-1)
print("after sorting the list of elements are:")
print(nums)
       
