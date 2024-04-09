# quick_sort _shortcut
# greek for greek

def quicksort(arr):
  if len(arr) <=1:
    return arr 
  else:
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

arr = [4, 6, 2, 5, 7, 9, 1, 3]
res = quicksort(arr)
print(res)
