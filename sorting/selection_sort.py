def selection_sort(arr):
  length = len(arr)
  for i in range(length-1):
    mini = i
    for j in range(i,length):
      if arr[j] < arr[mini]:
        mini = j
    arr[i],arr[mini] = arr[mini], arr[i]
    
  return arr
    
arr = [64, 25, 2, 22, 11]

res = selection_sort(arr)
print("sorted list : ")
print(res)
