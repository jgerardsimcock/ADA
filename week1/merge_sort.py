def merge(a,b):
  """This function merges two sorted lists. This is the part of the 
  algorithm that recombines the list and requires most of the creativity.
  We need to check to see if the value in index i of list a is less than value in index j of list b
  if so then we append to larger list, other wise we have to invert and append j to c. From whichever
  list we append from we need to increment the index up one."""

  i, j = 0, 0
  c = []

  while i < len(a) and j < len(b):
    if a[i] < b[j]:
      c.append(a[i])
      i += 1
    else:
      c.append(b[j])
      j += 1


  c += a[i:]# this appends the final value once the while condition ends
  c += b[j:]# this appends the final value once the while condition ends

  return c

  def merge_sort(sequence):
    """We run a recursive function call on this to break the merge_sort problem into smaller subroutines
    Then we merge upward until all the smaller units are properly sorted"""

    #We need a base case
    if len(sequence) == 1:
      return sequence

    else: 

      #we need to split into two sub sequences
      mid = int(len(sequence)/2) 
      head = merge_sort(seq[:mid])#first half of sequence
      tail = merge_sort(seq[mid:])#second half of sequence

      return merge(head,tail)





