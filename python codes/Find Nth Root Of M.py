def root_check(mid,n,m):
  ans = 1
  for i in range(1,n+1):
    ans *= mid
    if ans > m:
      return 2
  if ans == m:
    return 1
  return 0
def nroot(n,m):
  low = 1
  high = m
  
  while low <= high :
    mid = (low + high) // 2
    check = root_check(mid,n,m)
    
    if check == 1:
      return mid
    elif check == 0:
      low = mid + 1
      
    else:
      high = mid - 1
  
  return -1
  
  
n = 10
m = 3600
ans = nroot(n, m)
print("The answer is:", ans)
  
  
