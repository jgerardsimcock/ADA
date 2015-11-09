def merge_2d(a, b, axis = 0):

  """Function to merge two sorted arrays of 2-tuples.
  axis is coordinate from sort is based"""
  #We default the axis = 0 to the x value
  #We can put axis equals 1 to merge on the y value
  
  #similar to one dimensional sort we start with index values for each array

  i, j = 0, 0
  c =[]

  while i < len(a) and j < len(b):
    #if value of one vs another at that coordinate
    if a[i][axis] < b[j][axis]:
        c.append(a[i])
        i += 1

    else:
        c.append(b[j])
        j += 1


  c += a[i:]
  c += b[j:]

  return c


def merge_sort_2d(sequence, axis = 0):
  """recursive function to merge and sort"""

  #Base case to make sure sequence length is greater than 1
  if len(sequence) == 1:
    return sequence

  else: 

    mid = int(len(sequence)/ 2)

    head = merge_sort_2d(sequence[:mid], axis)
    tail = merge_sort_2d(sequence[mid:], axis)

    return merge_2d(head, tail, axis)


print merge_sort_2d([(1,9),(45,6),(7,25),(89,9),(76,39),(63,86),(0,37)])