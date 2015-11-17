def merge(a, b):
  """Take two sequences as unordered lists and orders them lowest to highest"""

  #We need index values to for each array
  i,j = 0, 0
  #We need an empty list to store the merged sequence
  c =[]
  inversions = 0

  #Iterate through each position in each array 
  while i < len(a) and j < len(b):

      if a[i] < b[j]:
        c.append(a[i])
        i += 1 #increment to next index value in a

      else:
        c.append(b[j])# be must be less and there is an inversion
        j +=1 
        inversions += len(a[i:])

  
  #once one list reaches its maximum the other array will still
  #have values left in it. We need to concatenate the remaining values to c

  c += a[i:]
  c += b[j:]

  print c, inversions
  return c, inversions


def merge_sort(sequence):
  """Here we split and combine"""

  if len(sequence) == 1:
    return sequence, 0

  else: 

    mid = len(sequence)/2
    head, s1 = merge_sort(sequence[:mid])
    tail, s2 = merge_sort(sequence[mid:])

    sorted_list, s3 = merge(head, tail)
    return sorted_list, (s1+s2+s3)


with open('data.txt') as f:
    alist = f.read().splitlines()
alist = [int(i) for i in alist]

#let's test

print merge_sort(alist)
