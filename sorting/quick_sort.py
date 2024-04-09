#quick_sort

def part(arr,low,high):
  pivot = arr[high]
  
  i = low - 1
  for j in range(low,high):
    if arr[j] <= pivot:
      i = i+1 
      arr[i],arr[j] = arr[j],arr[i]
  arr[i+1],arr[high] = arr[high],arr[i+1]
  return i+1
  
  
def quicksort(arr,low,high):
  if low < high:
    par = part(arr,low,high)
    quicksort(arr,low,par-1)
    quicksort(arr,par+1,high)

arr =  [4, 6, 2, 5, 7, 9, 1, 3]
n = len(arr)
res = quicksort(arr,0,n - 1)
print(arr)
