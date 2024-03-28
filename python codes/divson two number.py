
# example : 10 % 3
# ans : 3.33333....... but 
# print 3.(3)

# example : 1 / 1
# ans and print : 1

# if b is 0 then print("None")

def div(a,b):
  if b == 0:
    return None
  q = a//b
  r = a % b
  if r == 0:
    return q
    
  res = [str(q),"."]
  rem = {}
  while r !=0:
    if r in rem:
      res.insert(rem[r],"(")
      res.append(")")
      return "".join(res)
    rem[r] = len(res)
    r = r*10
    q = r // b
    res.append(str(q))
    r = r%b
  return "".join(res)
    
  

a = int(input())
b = int(input())

res = div(a,b)
print(res)
