# def quickSort(array):

#   less, equal, greater = [], [], []

#   if len(array) > 1:
#     pivot = array[0]

#     for val in array:
#       if array[val] < pivot:
#         less.append(array[val])

#       elif array[val] == pivot:
#         equal.append(array[val])

#       else:
#         greater.append(array[val])

#     quickSort(less)
#     quickSort(greater)

#     array_sorted = less + greater + equal
#     print array_sorted
#     return array_sorted


# def quickSort(array):
#   less = []
#   pivotList = []
#   more = []

#   if len(array) <= 1:
#     return array

#   else:
#     pivot = array[0]

#     for i in array:
#         if i < pivot: 
#           less.append(i)
#         elif i > pivot:
#           more.append(i)
#         else:
#           pivotList.append(i)

#     less = quickSort(less)
#     more = quickSort(more)
#     new_array = less + pivotList + more
#     print new_array
#     return new_array

def quickSortHelper(array):
  _quickSort(array, 0, len(array) - 1)
  print array 


def _quickSort(array, start, stop):

  if stop - start > 0:

    pivot = array[start]
    left = start
    right = stop
    comparisons = 0
    while left <= right:
        while array[left] < pivot:
          left += 1
          #comparisons += 1
        while array[right] > pivot:
          right -= 1
          comparisons += 1
        if left <= right: 
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
            #comparisons += 1
   
    _quickSort(array, start, right)
    _quickSort(array, left, stop)
    #return comparisons


array = [3,5,1,77,32,88,44,100,33,6,8]

quickSortHelper(array)