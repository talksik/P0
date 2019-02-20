def quicksort(arr):
  pivot = arr[0]
  for item in arr[1:]:
    if item > pivot:
      