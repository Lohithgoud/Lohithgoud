def allpossible(arr,mid):
  n = len(arr)
  student = 1
  pages = 0
  
  for i in range(n):
    if pages + arr[i] <= mid:
      pages += arr[i]
    else:
      student += 1
      pages += arr[i]
  
  return student
  
def booksallcote(arr,stds):
  n = len(arr)
  
  if stds > n:
    return -1
    
  low = max(arr)
  high = sum(arr)
  
  while low <= high:
    mid = (low + high) // 2
    
    if allpossible(arr,mid) > stds:
      low = mid + 1
    else:
      high = mid - 1
      
  return low    
  
  
  
arr = [5, 17, 100, 11]
stds = 4
ans = booksallcote(arr,stds)
print("The answer is:", ans)  
  

      
