
import time

def element_swap(array, index1, index2):
  """called by partition when the values at index1 and index2 need to be swapped"""

  #reassign the values
  array[index1], array [index2] = array[index2], array[index1]

def partition_head(array, head, tail):
  """Partitions an array with pivot point at array[0]
  all values less than array[0] will be placed to left of array[0]
  all values greater than array[0] will be on right

  head: partition start point

  tail: partition end point

  pointer: keeps track of partition between those values that are less than
  and those values that are greater than pivot

  Swap happens if an element is less than the pivot

  """

  pivot = array[head]
  pointer = head + 1

  for index in range(head+1, tail):
      if array[index] < pivot:
        element_swap(array, pointer, index)
        pointer += 1 #this points to the partition between the values
  element_swap(array, head, pointer -1)

  return pointer - 1

def quick_sort(array, head, tail):
  #base case
  if tail - head <=1:
    return 
  else:
    #subroutines
    pivot = partition_head(array, head,tail)
    #final 
    quick_sort(array, head, pivot)
    quick_sort(array , pivot+1,tail)


def main():

  array = [3,5,1,77,32,88,44,100,33,6,8]
  start_time = time.time()
  quick_sort(array, 0, len(array))
  print array
  print time.time() - start_time

if __name__ == '__main__':
  main()
