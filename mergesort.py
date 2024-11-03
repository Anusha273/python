def merge(nums,l,mid,r):
    n1 = mid - l + 1
    n2 = r - mid
    # Create temporary arrays
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = nums[l+i]
    for j in range(n2):
        R[j] = nums[mid+1+j]
    i=0
    j=0
    k=l
    while i < n1 and j < n2:
        if(L[i] <= R[j]):
            nums[k] = L[i]
            i += 1
        else:
            nums[k] = R[j]
            j += 1

        k += 1
    while i < n1 :
        nums[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        nums[k] = R[j]
        j += 1
        k += 1
    

def mergesort(nums, l, r):
    if(l < r):
        mid = l + (r-l) // 2
        mergesort(nums,l, mid)
        mergesort(nums,mid+1, r)
        merge(nums,l,mid,r)


n = int(input("Enter the number of elements: "))
nums = []
for i in range(n):
    nu = int(input())
    nums.append(nu)

print("Before sorting, the list of elements is:")
print(nums)

mergesort(nums, 0, n - 1)

print("After sorting, the list of elements is:")
print(nums)
