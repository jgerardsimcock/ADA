def _partition(array, start, end):
  count = 0
  pivot = start
  for i in xrange(start, end):
      count += 1
      if array[i] < array[end]:
        #Swap!
        array[i], array[pivot] = array[pivot], array[i]
        pivot += 1

  array[pivot], array[end] = array[end], array[pivot]
  return pivot, count

def _quickSort(array, start, end):
    count = 0
    if start < end:
      pivot, count = _partition(array, start, end)
      count += _quickSort(array,start, pivot - 1)
      count += _quickSort(array, pivot + 1, end)

    return count

def quickSort(array, start=None, end=None):
  if start is None:
    start = 0
  if end is None:
    end = len(array) - 1

  return _quickSort(array, start, end)



with open('Quicksort.txt') as f:
   alist = f.read().splitlines()

alist = [int(i) for i in alist]

count = quickSort(alist)
print alist, count
