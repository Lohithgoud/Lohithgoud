#insertion sort

arr = [64, 34, 25, 12, 2, 11, 90,1]

n = len(arr)

for i in range(n):
  j = i 
  while(j > 0 and arr[j-1] > arr[j]):
    arr[j-1],arr[j] = arr[j],arr[j-1]
    j-=1
    
print(arr)
